from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url ="https://api.npoint.io/674f5423f73deab1e9a7"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    # print(all_posts)
    return render_template("index.html", posts=all_posts)
    # return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

# title/subtitle/image/date/author/body
@app.route('/post/<int:blog_id>')
def post(blog_id):
    print(blog_id)
    blog_url ="https://api.npoint.io/674f5423f73deab1e9a7"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    # print(all_posts)
    posts_in = {}
    for blog_post in all_posts:
        if blog_post["id"] == blog_id:
            posts_in = blog_post
    return render_template("post.html", post=posts_in)


if __name__ == "__main__":
    app.run(debug=True)
