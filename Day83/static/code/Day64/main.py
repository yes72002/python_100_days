from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import json
from secret_key import API_READ_ACCESS_TOKEN
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
class Base(DeclarativeBase):
    pass

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"


# CREATE DB
db = SQLAlchemy(model_class=Base)
# initialize the app with the extension
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    # id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    # title: Mapped[str] = mapped_column(db.String(250), nullable=False, unique=True)
    # author: Mapped[str] = mapped_column(db.String(250), nullable=False)
    # rating: Mapped[float] = mapped_column(nullable=False)
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    title: Mapped[str] = mapped_column(db.String(250), nullable=False, unique=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(db.String(250), nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(db.String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(db.String(250), nullable=False)

# Create the database and the movies table
with app.app_context():
    db.create_all()

# with app.app_context():
#     # Create a new book entry and add it
#     new_movie = Movie(
#         title="Phone Booth",
#         year=2002,
#         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#         rating=7.3,
#         ranking=10,
#         review="My favourite character was the caller.",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#     )
#     db.session.add(new_movie)
#     db.session.commit()
#     print("New movie entry has been created successfully!")
zero_movie = Movie(
    title="Drive",
    year=2011,
    description="A mysterious Hollywood stuntman and mechanic moonlights as a getaway driver and finds himself in trouble when he helps out his neighbor in this action drama.",
    rating=7.5,
    ranking=9,
    review="Loved it!",
    img_url="https://www.shortlist.com/media/images/2019/05/the-30-coolest-alternative-movie-posters-ever-2-1556670563-K61a-column-width-inline.jpg"
)
first_movie = Movie(
        title="Phone Booth",
        year=2002,
        description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
        rating=7.3,
        ranking=10,
        review="My favourite character was the caller.",
        img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    )
second_movie = Movie(
    title="Avatar The Way of Water",
    year=2022,
    description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    rating=7.3,
    ranking=9,
    review="I liked the water.",
    img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
)


def add_new_movie(new_movie):
    with app.app_context():
        db.session.add(new_movie)
        db.session.commit()
        print("New movie entry has been created successfully!")

# add_new_movie(zero_movie)
# add_new_movie(first_movie)
# add_new_movie(second_movie)

# Form
class Editform(FlaskForm):
    rating = StringField('Your rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField(label="Done")

class Addform(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.ranking)).scalars()
    return render_template("index.html", all_movies=all_movies)

@app.route("/edit?/id=<int:id>", methods=["GET", "POST"])
def edit(id):
    edit_form = Editform()
    if edit_form.validate_on_submit():
        new_rating = float(edit_form.rating.data)
        new_review = edit_form.review.data
        # update to the database
        movie_to_update = db.get_or_404(Movie, id)
        movie_to_update.rating = new_rating
        movie_to_update.review = new_review
        db.session.commit()
        print("New rating has been updated successfully!")
        return redirect(url_for('home'))
    else:
        return render_template("edit.html", form=edit_form)

@app.route("/delete/id=<int:id>", methods=["GET", "POST"])
def delete(id):
    movie_to_delete = db.get_or_404(Movie, id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))



@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = Addform()
    if request.method == "POST":
        movie_title = request.form['title']
        url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}&include_adult=true&language=en-US&page=1"
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer " + API_READ_ACCESS_TOKEN
        }
        response = requests.get(url, headers=headers)
        search_movies = response.json()
        search_movies = search_movies["results"]
        # print(search_movies)
        return render_template("select.html", search_movies=search_movies)
    else:
        return render_template("add.html", form=add_form)

@app.route("/find", methods=["GET", "POST"])
def find_movie():
    movie_id = request.args.get("id")
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + API_READ_ACCESS_TOKEN
    }
    response = requests.get(url, headers=headers)
    # print(response.text)
    movie = response.json()
    movie_title = movie["title"]
    print(movie["release_date"])
    movie_year = movie["release_date"].split('-')[0]
    movie_description = movie["overview"]
    movie_img_url = "https://image.tmdb.org/t/p/w500" + movie["backdrop_path"]

    edit_form = Editform()
    if edit_form.validate_on_submit():
        new_rating = float(edit_form.rating.data)
        new_review = edit_form.review.data
        # add movie to the database
        new_movie = Movie(
            title = movie_title,
            year = movie_year,
            description = movie_description,
            rating = new_rating,
            ranking = 10,
            review = new_review,
            img_url = movie_img_url,
        )
        db.session.add(new_movie)
        db.session.commit()
        print("New movie has been added successfully!")
        return redirect(url_for('home'))
    else:
        # return redirect(url_for('home'))
        return render_template("edit.html", form=edit_form)


if __name__ == '__main__':
    app.run(debug=True)
