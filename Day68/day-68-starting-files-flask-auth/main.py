from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from wtforms.validators import DataRequired, URL, Email
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # return User.get(user_id) # flask-login's code
    return User.query.get(int(user_id)) # Jim's code
    return db.get_or_404(User, user_id) # Angela's code

# CREATE TABLE IN DB
class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # email: Mapped[str] = mapped_column(String(100), unique=True)
    email: Mapped[str] = mapped_column(String(100), unique=False)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
    # is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    def is_authenticated(self):
        # Check if the user is authenticated
        return True  # You should implement the logic to check authentication based on provided credentials
    def get_id(self):
        # Return the unique identifier for the user
        return self.id
    def is_active(self):
        # Check if the user is active
        return self.is_active

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        new_name     = request.form['name']
        new_email    = request.form['email']
        new_password = request.form['password']
        hashed_password = generate_password_hash(new_password, method='pbkdf2:sha256', salt_length=8)

        new_user = User(
            name     = new_name,
            email    = new_email,
            password = hashed_password,
        )

        user = db.session.execute(db.select(User).where(User.email == new_email)).scalar()
        if user:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        db.session.add(new_user)
        db.session.commit()

        # Log in and authenticate user after adding details to database.
        login_user(new_user)

        return render_template("secrets.html", name=new_name)
    else:
        return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    # form = LoginForm()
    # if form.validate_on_submit():
    if request.method == 'POST':
        new_email    = request.form['email']
        new_password = request.form['password']
        print(new_email)
        print(new_password)

        # Query the database to find the user by email (Find the user)
        user = User.query.filter_by(email=new_email).first()
        print(user)

        # Check if a user with the provided email exists and if the password matches
        if user:
            if user.password == new_password:
            # if user and check_password_hash(user.password, new_password):
                login_user(user) # Log in the user
                print('Logged in successfully.')
                next = request.args.get('next')
                return redirect(next or url_for('secrets'))
            else:
                flash('Password incorrect. please try again.')
        else:
            flash('That email does not exist, please try again.')
    return render_template('login.html')

@app.route('/secrets')
@login_required
def secrets():
    if current_user.is_authenticated:
        # Get the logged-in user's name
        user_name = current_user.name
        return render_template('secrets.html', name=user_name)
    else:
        # Handle the case where the user is not logged in
        return "Please log in to access your profile.", 401  # Unauthorized status code

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/download/')
@login_required
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
