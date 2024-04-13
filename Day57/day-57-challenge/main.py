from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello World!</h1>"

@app.route('/guess/<name>')
def guess(name):
    agify_response = requests.get(url=f"https://api.agify.io/?name={name}")
    agify_data = agify_response.json()
    # print(agify_data)
    # print(agify_data['age'])
    age = agify_data['age']

    genderize_response = requests.get(url=f"https://api.genderize.io/?name={name}")
    genderize_data = genderize_response.json()
    # print(genderize_data)
    # print(genderize_data['gender'])
    gender = genderize_data['gender']

    return render_template('index.html', name=name, age=age, gender=gender)

@app.route('/blog/<num>')
def blog(num):
    print(num)
    blog_url ="https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    print(all_posts)
    return render_template('blog.html', posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
