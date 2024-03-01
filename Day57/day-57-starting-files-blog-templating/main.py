from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_url ="https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    # print(all_posts)
    return render_template('index.html', posts=all_posts)

@app.route('/blog/post/<blog_id>')
def get_post(blog_id):
    print(blog_id)
    blog_url ="https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    # print(all_posts)
    posts_in = {}
    for blog_post in all_posts:
        # print(type(blog_id)) # str        
        if blog_post["id"] == int(blog_id):
            posts_in = blog_post
    return render_template('post.html', post=posts_in)


if __name__ == "__main__":
    app.run(debug=True)



