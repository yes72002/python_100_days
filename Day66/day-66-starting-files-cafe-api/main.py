from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from sqlalchemy import func

import random
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
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


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    # print(random_cafe)
    if random_cafe:
        # exist
        return jsonify(cafe = random_cafe.to_dict())
        return jsonify({
            "cafe": {
                "name"           : random_cafe.name,
                "map_url"        : random_cafe.map_url,
                "img_url"        : random_cafe.img_url,
                "location"       : random_cafe.location,
                "seats"          : random_cafe.seats,
                "has_toilet"     : random_cafe.has_toilet,
                "has_wifi"       : random_cafe.has_wifi,
                "has_sockets"    : random_cafe.has_sockets,
                "can_take_calls" : random_cafe.can_take_calls,
                "coffee_price"   : random_cafe.coffee_price,
            }
        })
    else:
        return "No cafes found in the database"

@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    # random_cafe = random.choice(all_cafes)
    # print(random_cafe)
    # print(all_cafes)
    all_cafes = [cafe.to_dict() for cafe in all_cafes]
    # print(all_cafes)
    if all_cafes:
        return jsonify(cafe = all_cafes)
    else:
        return "No cafes found in the database"

@app.route("/search")
def get_one_cafes():
    loc = request.args.get('loc')
    print(f"loc = {loc}")
    # scalar() for one result
    # cafe = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalar()
    # print(cafe)
    # if cafe:
    #     return jsonify(cafe = cafe)
    # else:
    #     return jsonify(error = {"Not Found":"Sorry, we don't have a cafe at the location."})
    # scalars() for one result
    all_cafes = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars()
    all_cafes = [cafe.to_dict() for cafe in all_cafes]
    if all_cafes:
        return jsonify(cafe = all_cafes)
    else:
        return jsonify(error = {"Not Found":"Sorry, we don't have a cafe at the location."})

# HTTP POST - Create Record
@app.route("/add", methods=["GET", "POST"])
def add_one_cafe():
    new_cafe = Cafe(
        name           = request.form.get("name"),
        map_url        = request.form.get("map_url"),
        img_url        = request.form.get("img_url"),
        location       = request.form.get("location"),
        seats          = request.form.get("seats"),
        has_toilet     = bool(request.form.get("has_toilet")),
        has_wifi       = bool(request.form.get("has_wifi")),
        has_sockets    = bool(request.form.get("has_sockets")),
        can_take_calls = bool(request.form.get("can_take_calls")),
        coffee_price   = request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    
    return jsonify(repsonce = {"Success":"Successful added the new cafe."})

# HTTP PUT/PATCH - Update Record
# # http://127.0.0.1:5000/update-price?cafe_id=1&new_price=5.99
# @app.route("/update-price", methods=["GET", "POST"])
# def update_price():
#     cafe_id = request.args.get('cafe_id')
#     new_price = request.args.get('new_price')
#     print(cafe_id)
#     print(new_price)
#     # Verify if both variables are present
#     if cafe_id is None or new_price is None:
#         return jsonify(erroe={"error": "Both 'cafe_id' and 'new_price' parameters are required."}), 400
#     # Retrieve the cafe to update from the database
#     cafe_to_update = db.get_or_404(Cafe, cafe_id)
#     if cafe_to_update:
#         # Update the coffee price of the cafe
#         cafe_to_update.coffee_price = new_price
#         # Commit the changes to the database
#         db.session.commit()
#         return jsonify(repsonce = {"Success":"Successful updated the price."})
#     else:
#         return jsonify(error={"Not found": "Sorry a cafe with that id was not found in the database."})

# /update-price/22?new_price=5.99
@app.route("/update-price/<int:cafe_id>", methods=["GET", "POST"])
def update_price(cafe_id):
    new_price = request.args.get('new_price')
    print(cafe_id)
    print(new_price)
    # Verify if both variables are present
    if cafe_id is None or new_price is None:
        return jsonify(erroe={"error": "Both 'cafe_id' and 'new_price' parameters are required."}), 400
    # Retrieve the cafe to update from the database
    cafe_to_update = db.get_or_404(Cafe, cafe_id)
    if cafe_to_update:
        # Update the coffee price of the cafe
        cafe_to_update.coffee_price = new_price
        # Commit the changes to the database
        db.session.commit()
        return jsonify(repsonce = {"Success":"Successful updated the price."})
    else:
        return jsonify(error={"Not found": "Sorry a cafe with that id was not found in the database."})

# HTTP DELETE - Delete Record
# /report-closed/1?api-key=TopSecretAPIKey
@app.route("/report-closed/<int:cafe_id>", methods=["GET", "POST"])
def delete(cafe_id):
    api_key = request.args.get('api-key')
    # cafe_to_delete = db.get_or_404(Cafe, cafe_id)
    cafe_to_delete = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    if cafe_to_delete is None:
        return jsonify(error={"Not found": "Sorry a cafe with that id was not found in the database."})
    else:
        if api_key == "TopSecretAPIKey":
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(repsonce = {"Success":"Successful deleted the cafe."})
        else:
            return jsonify({"error":"Sorry, that's not allowed. Make sure you have the correct api_key."})

if __name__ == '__main__':
    app.run(debug=True)
