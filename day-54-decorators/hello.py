from flask import Flask
import time
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World'

@app.route('/bye')
def say_goodbye():
    return "SEE YA!"

if __name__ == "__main__":
    app.run()

# -- DECORATORS
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         # Do something before
#         function()
#         # Do something after
#     return wrapper_function

# @delay_decorator
# def say_hello():
#     print("Hello")

# @delay_decorator
# def say_goodbye():
#     print("Goodbye")

# say_hello()
# say_goodbye()