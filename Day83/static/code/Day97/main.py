from flask import Flask, render_template, redirect, url_for, request, abort, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text, Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditor, CKEditorField
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from forms import CreatePostForm, RegisterForm, LoginForm

class Base(DeclarativeBase):
    pass

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

def admin_only(function):
    @wraps(function)
    def wrapper_function(*args, **kwargs):
        if current_user.is_authenticated and current_user.id == 1:
            return function(*args, **kwargs)
        else:
            abort(403)
    return wrapper_function

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)
    name: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()

@app.route('/', methods=["GET", "POST"])
def get_all_cafes():
    return render_template("index.html")

@app.route('/view-cafe', methods=["GET", "POST"])
def view_cafe():
    coffee_name = request.form.get('coffee_name')
    print(f"coffee_name = {coffee_name}")
    small_price = request.form.get('small_price')
    print(f"small_price = {small_price}")
    small_num = request.form.get('small_num')
    print(f"small_num = {small_num}")
    large_price = request.form.get('large_price')
    print(f"large_price = {large_price}")
    large_num = request.form.get('large_num')
    print(f"large_num = {large_num}")
    if small_num in ["1","2","3"]:
        small_num = int(small_num)
    else:
        small_num = 1
    if large_num in ["1","2","3"]:
        large_num = int(large_num)
    else:
        large_num = 1

    return render_template("view-cafe.html", coffee_name=coffee_name, small_price=small_price, small_num=small_num,large_price=large_price, large_num=large_num)

@app.route('/buy-cafe', methods=["GET", "POST"])
def buy_cafe():
    coffee_name = request.form.get('coffee_name')
    print(f"coffee_name = {coffee_name}")
    small_price = request.form.get('small_price')
    print(f"small_price = {small_price}")
    small_num = request.form.get('small_num')
    print(f"small_num = {small_num}")
    large_price = request.form.get('large_price')
    print(f"large_price = {large_price}")
    large_num = request.form.get('large_num')
    print(f"large_num = {large_num}")

    return render_template("buy-cafe.html", coffee_name=coffee_name, small_price=small_price, small_num=small_num,large_price=large_price, large_num=large_num)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods=["GET", "POST"])
def register():
    register_from = RegisterForm()
    if request.method == 'POST':
        new_email    = register_from.email.data
        new_password = register_from.password.data
        new_name     = register_from.name.data

        hashed_password = generate_password_hash(new_password, method='pbkdf2:sha256', salt_length=8)
        hashed_password = new_password

        new_user = User(
            email    = new_email,
            password = hashed_password,
            name     = new_name,
        )

        user = db.session.execute(db.select(User).where(User.email == new_email)).scalar()
        if user:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        db.session.add(new_user)
        db.session.commit()

        # Log in and authenticate user after adding details to database.
        login_user(new_user)

        return redirect(url_for('get_all_cafes'))
    else:
        return render_template("register.html", form=register_from)

# Retrieve a user from the database based on their email.
@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        new_email    = request.form['email']
        new_password = request.form['password']
        print(f"login_email = {new_email}")
        print(f"login_password = {new_password}")

        # Query the database to find the user by email (Find the user)
        user = db.session.execute(db.select(User).where(User.email == new_email)).scalar()
        print(user)

        # Check if a user with the provided email exists and if the password matches
        if user:
            if user.password == new_password:
            # if user and check_password_hash(user.password, new_password):
                login_user(user) # Log in the user
                print('Logged in successfully.')
                return redirect(url_for('get_all_cafes'))
            else:
                flash('Password incorrect. please try again.')
        else:
            flash('That email does not exist, please try again.')
    return render_template('login.html', form=login_form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_cafes'))


if __name__ == "__main__":
    app.run(debug=True, port=5003)
