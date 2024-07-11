def add(*args): #args is for a list
    sum = 0
    for number in args:
        sum += number
    print(sum)

add(9,3,4,5,6)

def calculate(n, **kwargs): #kwargs is for a dictionary
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(kwargs[])


calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')

my_car = Car(make="Honda", model="Civic")
print(my_car.model)