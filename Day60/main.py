from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username)
        print(password)
    # return 0
    # return render_template('login.html', username, password)
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
