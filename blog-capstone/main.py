from post import Post
import requests

from flask import Flask
app = Flask(__name__)
from flask import render_template

app = Flask(__name__)
post_list = []

@app.route('/')
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url) 
    all_posts = response.json()
    for post in all_posts:
        blog_post = Post(
        title = post["title"],
        subtitle = post["subtitle"],
        id = post["id"],
        body = post["body"]
        )
        post_list.append(blog_post)
    return render_template("index.html", posts=post_list)

@app.route('/post/<id>')
def get_post(id):
    title = (get_info(id, post_list)).title
    subtitle = (get_info(id, post_list)).title
    body = (get_info(id, post_list)).body
    return render_template("post.html", num=id, t=title, sub=subtitle, bod=body)

def get_info(id, post_list):
    id = int(id)
    return post_list[id - 1]

if __name__ == "__main__":
    app.run(debug=True)
