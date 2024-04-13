from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

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

# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"

# create database
db = SQLAlchemy(model_class=Base)
# initialize the app with the extension
db.init_app(app)

# Define a model class for the books table
class Book(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    title: Mapped[str] = mapped_column(db.String(250), nullable=False, unique=True)
    author: Mapped[str] = mapped_column(db.String(250), nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)

# Create the database and the books table
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template("index.html", all_books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_name = request.form['book_name']
        book_author = request.form['book_author']
        rating = request.form['rating']
        # print(book_name)
        # print(book_author)
        # print(rating)
        new_book = Book(title=book_name, author=book_author, rating=rating)
        db.session.add(new_book)
        db.session.commit()
        print("New book entry has been created successfully!")

        # method 1
        # result = db.session.execute(db.select(Book).order_by(Book.title))
        # all_books = result.scalars()
        # return render_template("index.html", all_books=all_books)
        # method 2
        return redirect(url_for('home'))
    else:
        return render_template("add.html")

@app.route("/edit?/id=<int:id>", methods=["GET", "POST"])
def edit(id):
    book = db.session.execute(db.select(Book).where(Book.id == id)).scalar()

    if request.method == "POST":
        new_rating = request.form['new_rating']
        # print(type(new_rating)) # <class 'str'>
        book_to_update = db.get_or_404(Book, id)
        book_to_update.rating = float(new_rating)
        db.session.commit()
        print("New rating has been updated successfully!")

        # method 1
        # result = db.session.execute(db.select(Book).order_by(Book.title))
        # all_books = result.scalars()
        # return render_template("index.html", all_books=all_books)
        # method 2
        return redirect(url_for('home'))
    else:
        return render_template("edit.html", book=book)

@app.route("/delete/id=<int:id>", methods=["GET", "POST"])
def delete(id):
    book_to_delete = db.get_or_404(Book, id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

