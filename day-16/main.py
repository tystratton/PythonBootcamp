# import another_module

# print(another_module.another_variable)

# from turtle import Turtle, Screen

# timmy = Turtle()
# my_screen = Screen()


# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# print(timmy)
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon", ["Bulbasaur", "Torchic", "Gengar"])
table.add_column("Type", ["Grass/Poison", "Fire", "Ghost"])
table.align = "l"
print(table)