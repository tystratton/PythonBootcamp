from flask import Flask
app = Flask(__name__)
from flask import render_template
import requests

class Blog:
    def __init__(self, id, body, title, subtitle, image_url):
        self.id = id
        self.body = body
        self.title = title
        self.subtitle = subtitle
        self.image_url = image_url

blog_posts = []
endpoint = 'https://api.npoint.io/674f5423f73deab1e9a7'
response= requests.get(url=endpoint)
data = response.json()
for post in data:
    blog = Blog(
    id = post.get("id"),
    body = post.get("body"),
    title = post.get("title"),
    subtitle = post.get("subtitle"),
    image_url = post.get("image_url")
    )
    blog_posts.append(blog)


@app.route('/')
def home():
    return render_template('index.html', posts=blog_posts)

@app.route('/about')
def get_about():
    return render_template('about.html')

@app.route('/contact')
def get_contact():
    return render_template('contact.html')

@app.route('/blog/<id>')
def get_post(id):
    id = int(id)
    for post in blog_posts:
        if post.id == id:
            blogId = id
    return render_template("post.html", post=blog_posts[blogId])

if __name__ == "__main__":
    app.run(debug=True) #allows you to update live server

#{{ url_for('get_blog', num=3) }}

