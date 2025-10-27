import turtle
turtle.pendown()
turtle.delay(0)
turtle.speed(0)


def kochLine(level, length):
    if level == 1:
        turtle.forward(length)
    else:
        kochLine(level-1, length/3)
        turtle.left(60)
        kochLine(level-1, length/3)
        turtle.right(120)
        kochLine(level-1, length/3)
        turtle.left(60)
        kochLine(level-1, length/3)
    
def kochSnowflake(level, length):
    kochLine(level, length)
    turtle.right(120)
    kochLine(level, length)
    turtle.right(120)
    kochLine(level, length)
    turtle.right(120)

kochSnowflake(5, 700)
turtle.done()