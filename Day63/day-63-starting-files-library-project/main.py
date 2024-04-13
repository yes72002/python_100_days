from flask import Flask, render_template, request, redirect, url_for

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

all_books = []

@app.route('/')
def home():
    books_num = len(all_books)
    return render_template("index.html", all_books=all_books, books_num=books_num)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_name = request.form['book_name']
        book_author = request.form['book_author']
        rating = request.form['rating']
        print(book_name)
        print(book_author)
        print(rating)
        book_dict = {}
        book_dict["title"] = book_name
        book_dict["author"] = book_author
        book_dict["rating"] = rating
        print(book_dict)
        all_books.append(book_dict)
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

