from flask import Flask, render_template
import random
# from datetime import date
# from datetime import datetime
import datetime

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    today = datetime.date.today()
    current_year = datetime.datetime.now().year
    print("Today's date:", current_year)
    # print("Today's date:", today)
    return render_template('index.html', num=random_number, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)


