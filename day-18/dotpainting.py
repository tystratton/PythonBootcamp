from turtle import Turtle, Screen
import colorgram
import random

timmy = Turtle()
timmy.penup()
timmy.setpos(-200,200)
timmy.pendown()
timmy.shape("arrow")
timmy.color("blue")
timmy.pen(pensize = 20, speed = 0)
screen = Screen()
screen.colormode(255)
screen.colormode()
colors = colorgram.extract('painting.jpg', 10)

# Extracting colors from images and making dot painting
# height = 10
# width = 10
# count = 0
# count_height = 0
# snake = False
# while count_height <= height:
#     while count <= width:
#         color = colors[random.randint(0,9)]
#         timmy.pencolor(color.rgb)
#         timmy.pendown()
#         if snake == False:
#             timmy.circle(5)
#             timmy.penup()
#             timmy.forward(80)
#         else:
#             timmy.circle(5)
#             timmy.penup()
#             timmy.forward(-80)
#         count+=1
#     timmy.right(90)
#     timmy.forward(80)
#     timmy.left(90)
#     if snake == False:
#         snake = True
#         timmy.forward(-80)
#     else:
#         snake = False
#         timmy.forward(80)
#     count = 0
#     count_height += 1



#spinograph
go = True
side = 0
while go == True:
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    timmy.pencolor(r,g,b)
    timmy.circle(80)
    timmy.right(10)
        

# Random walk
# go = True
# while go == True:
#     r = random.randint(1,255)
#     g = random.randint(1,255)
#     b = random.randint(1,255)
#     timmy.pencolor(r,g,b)
#     direction = random.randint(1,4)
#     timmy.forward(30)
#     timmy.right(90*direction)

# draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon
# def screensaver():
#     sides = 3
#     count = 0
#     while sides < 10:
#         while count != sides:
#             timmy.forward(100)
#             timmy.right(360/sides)
#             count+=1
#         count = 0
#         sides+=1
#         r = random.randint(1,255)
#         g = random.randint(1,255)
#         b = random.randint(1,255)
#         timmy.pencolor(r,g,b)

# screensaver()




# dashed line
# count = 0
# fill = True
# while count < 10:
#     if fill == True:
#         timmy.pendown()
#         timmy.forward(5)
#         fill = False
#     elif fill == False:
#         timmy.penup()
#         timmy.forward(5)
#         fill = True
#     count+=1

# Draw a square
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)

screen.exitonclick()