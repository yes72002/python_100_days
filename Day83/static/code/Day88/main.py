from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField

'''
Make sure the required packages are installed:
Open the Terminal in PyCharm (bottom left).

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CONFIGURE TABLE
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class CafeForm(FlaskForm):
    name = StringField('Cafe Name', validators=[DataRequired()])
    map_url = StringField('Map URL', validators=[DataRequired()])
    # img_url = StringField('Blog Image URL', validators=[DataRequired(), URL()])
    img_url = StringField('Blog Image URL', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    seats = StringField('Seats', validators=[DataRequired()])
    has_toilet = BooleanField('has_toilet', validators=[DataRequired()])
    has_wifi = BooleanField('has_wifi', validators=[DataRequired()])
    has_sockets = BooleanField('has_sockets', validators=[DataRequired()])
    can_take_calls = BooleanField('can_take_calls', validators=[DataRequired()])
    coffee_price = StringField('Coffee Price (£2.75)', validators=[DataRequired()])
    submit = SubmitField('Submit')

with app.app_context():
    db.create_all()

@app.route('/')
def get_all_cafes():
    # Query the database for all the cafes. Convert the data to a python list.
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    # print(all_cafes)
    cafes = all_cafes
    return render_template("index.html", all_cafes=cafes)

# Add a route so that you can click on individual cafes.
@app.route('/<cafe_id>')
def show_cafe(cafe_id):
    # Retrieve a Cafe from the database based on the cafe_id
    requested_cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    # requested_cafe = "Grab the cafe from your database"
    return render_template("cafe.html", cafe=requested_cafe)

# add_new_cafe() to create a new blog cafe
@app.route('/new-cafe', methods=["GET", "POST"])
def add_new_cafe():
    add_form = CafeForm()
    if request.method == 'POST':
        new_name           = add_form.name.data
        new_map_url        = add_form.map_url.data
        new_img_url        = add_form.img_url.data
        new_location       = add_form.location.data
        new_seats          = add_form.seats.data
        new_has_toilet     = add_form.has_toilet.data
        new_has_wifi       = add_form.has_wifi.data
        new_has_sockets    = add_form.has_sockets.data
        new_can_take_calls = add_form.can_take_calls.data
        new_coffee_price   = add_form.coffee_price.data
        new_cafe = Cafe(
            name           = new_name,
            map_url        = new_map_url,
            img_url        = new_img_url,
            location       = new_location,
            seats          = new_seats,
            has_toilet     = new_has_toilet,
            has_wifi       = new_has_wifi,
            has_sockets    = new_has_sockets,
            can_take_calls = new_can_take_calls,
            coffee_price   = new_coffee_price,
        )

        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('get_all_cafes'))
    else:
        return render_template("make-cafe.html", form=add_form, post_h1="New Cafe")

# edit_cafe() to change an existing blog cafe
@app.route('/edit-cafe/<int:cafe_id>', methods=["GET", "POST"])
def edit_cafe(cafe_id):
    cafe_to_update = db.get_or_404(Cafe, cafe_id)
    edit_form = CafeForm(
        name=cafe_to_update.name,
        map_url=cafe_to_update.map_url,
        img_url=cafe_to_update.img_url,
        location=cafe_to_update.location,
        seats=cafe_to_update.seats,
        has_toilet=cafe_to_update.has_toilet,
        has_wifi=cafe_to_update.has_wifi,
        has_sockets=cafe_to_update.has_sockets,
        can_take_calls=cafe_to_update.can_take_calls,
        coffee_price=cafe_to_update.coffee_price,
    )
    if request.method == 'POST':
        new_name           = edit_form.name.data
        new_map_url        = edit_form.map_url.data
        new_img_url        = edit_form.img_url.data
        new_location       = edit_form.location.data
        new_seats          = edit_form.seats.data
        new_has_toilet     = edit_form.has_toilet.data
        new_has_wifi       = edit_form.has_wifi.data
        new_has_sockets    = edit_form.has_sockets.data
        new_can_take_calls = edit_form.can_take_calls.data
        new_coffee_price   = edit_form.coffee_price.data
        cafe_to_update.name           = new_name
        cafe_to_update.map_url        = new_map_url
        cafe_to_update.img_url        = new_img_url
        cafe_to_update.location       = new_location
        cafe_to_update.seats          = new_seats
        cafe_to_update.has_toilet     = new_has_toilet
        cafe_to_update.has_wifi       = new_has_wifi
        cafe_to_update.has_sockets    = new_has_sockets
        cafe_to_update.can_take_calls = new_can_take_calls
        cafe_to_update.coffee_price   = new_coffee_price
        db.session.commit()
        return redirect(url_for('get_all_cafes'))
    else:
        return render_template("make-cafe.html", form=edit_form, post_h1="Edit Cafe")

# delete_cafe() to remove a blog cafe from the database
@app.route('/delete/<int:cafe_id>', methods=["GET", "POST"])
def delete_cafe(cafe_id):
    cafe_to_delete = db.get_or_404(Cafe, cafe_id)
    db.session.delete(cafe_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_cafes'))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
