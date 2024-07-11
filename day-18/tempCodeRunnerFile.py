go = True
side = 0
while go == True:
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    timmy.pencolor(r,g,b)
    timmy.circle(80)
    timmy.right(10)