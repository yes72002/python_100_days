# import sqlite3

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()

# Create Tables in our Database
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# Add data to our table
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()



from flask import Flask, render_template, request, redirect
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

class Base(DeclarativeBase):
    pass

# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

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

with app.app_context():
    # Create a new book entry and add it
    new_book = Book(id=2, title='Harry Potter2', author='J. K. Rowling', rating=9.3)
    db.session.add(new_book)
    db.session.commit()
    print("New book entry has been created successfully!")
