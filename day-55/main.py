from flask import Flask
import random
app = Flask(__name__)

random_number = random.randint(0,9)

def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

@app.route('/bye')
@make_bold
def bye():
    return 'Bye!'

@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>\
        <img src="https://cdn.7tv.app/emote/01EZY967K0000CYST6006V20T8/4x.avif" width=500>'

@app.route("/<int:number>")
def guess(number):
    if number > 9 or number < 0:
        return '<h1> BETWEEN 0 and 9 PLEASE </h1>\
                <img src="https://cdn.7tv.app/emote/01F6BN89H80006VBW12DRB1DJ0/4x.avif" width=500>'
    elif number == random_number:
        return '<h1> CORRECT! </h1>\
                <img src="https://cdn.7tv.app/emote/01F6MQ33FG000FFJ97ZB8MWV52/4x.avif" width=500>'
    elif number > random_number:
        return '<h1> TOO HIGH! </h1>\
                <img src="https://cdn.7tv.app/emote/01F6FTE8B80008E39HFFQJ7MWS/4x.avif" width=500>'
    else:
        return '<h1> TOO LOW! </h1>\
                <img src="https://cdn.7tv.app/emote/01GBPSCGR00007Q17796BDN5AJ/4x.avif" width=500>'

if __name__ == "__main__":
    app.run(debug=True) #allows you to update live server
