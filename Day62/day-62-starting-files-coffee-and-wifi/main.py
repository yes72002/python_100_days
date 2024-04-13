from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
from flask_bootstrap import Bootstrap5, Bootstrap4

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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

class CafeForm(FlaskForm):
    coffee_choices = [
        ('☕️', '☕️'), 
        ('☕️☕️', '☕️☕️'), 
        ('☕️☕️☕️', '☕️☕️☕️'), 
        ('☕️☕️☕️☕️', '☕️☕️☕️☕️'), 
        ('☕️☕️☕️☕️☕️', '☕️☕️☕️☕️☕️')]
    wifi_choices = [
        ('✘', '✘'), 
        ('💪', '💪'), 
        ('💪💪', '💪💪'), 
        ('💪💪💪', '💪💪💪'), 
        ('💪💪💪💪', '💪💪💪💪'), 
        ('💪💪💪💪💪', '💪💪💪💪💪')
    ]
    power_choices = [
        ('✘', '✘'), 
        ('🔌', '🔌'), 
        ('🔌🔌', '🔌🔌'), 
        ('🔌🔌🔌', '🔌🔌🔌'), 
        ('🔌🔌🔌🔌', '🔌🔌🔌🔌'), 
        ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')
    ]
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(),URL()])
    opening = StringField('Opening Time e.g. 8AM.', validators=[DataRequired()])
    closing = StringField('Closing Time e.g. 5:30PM.', validators=[DataRequired()])
    coffee = SelectField('Coffee Rating', choices=coffee_choices, validators=[DataRequired()])
    wifi = SelectField('Wifi Strength Rating', choices=wifi_choices, validators=[DataRequired()])
    power = SelectField('Power Socket Availability', choices=power_choices, validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    if form.validate_on_submit():
        print("True")
        cafe = form.cafe.data
        location = form.location.data
        opening = form.opening.data
        closing = form.closing.data
        coffee = form.coffee.data
        wifi = form.wifi.data
        power = form.power.data
        data_to_append = [cafe, location, opening, closing, coffee, wifi, power]
        print(data_to_append)
        with open('cafe-data.csv', 'a', newline='', encoding='utf-8') as file:
            # Create a CSV writer object
            writer = csv.writer(file)
            # Write the data to the CSV file
            writer.writerow(data_to_append)
        print("True")
    return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
