from flask import Flask
app = Flask(__name__)
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True) #allows you to update live server
