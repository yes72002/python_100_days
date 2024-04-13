from flask import Flask
from flask import render_template

app = Flask(__name__)
# print(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')
    # return render_template('angela.html')


if __name__ == "__main__":
    app.run(debug=True)
