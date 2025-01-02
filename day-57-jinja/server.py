import random
import requests
from datetime import datetime

from flask import Flask
app = Flask(__name__)
from flask import render_template

@app.route('/guess/<name>')
def home(name):
    endpoint = 'https://api.agify.io?name=' + name
    response= requests.get(url=endpoint)
    data = response.json()
    age = data.get("age")
    random_number = random.randint(1,10)
    current_year = datetime.now().year
    return render_template('index.html', n=name, age=age, num=random_number, year=current_year)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url) 
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True) #allows you to update live server
