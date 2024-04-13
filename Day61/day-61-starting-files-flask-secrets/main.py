from flask import Flask, render_template, request
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5, Bootstrap4

class MyForm(FlaskForm):
    email = StringField(label='Email',validators=[DataRequired(), Email()])
    password  = PasswordField(label='Password',validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log in")

app = Flask(__name__)
app.config['SECRET_KEY']='mykey'
# app.secret_key = "any-string-you-want-just-keep-it-secret"

bootstrap = Bootstrap4(app)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    email = False
    password = False
    # form為類別的實體
    form = MyForm()
    if form.validate_on_submit():
        # 取出email/password欄位的輸入值
        email = form.email.data
        password = form.password.data
        if email == "admin@email.com" and password == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    else:
        return render_template('login.html', form=form,email=email,password=password)


if __name__ == '__main__':
    app.run(debug=True)

