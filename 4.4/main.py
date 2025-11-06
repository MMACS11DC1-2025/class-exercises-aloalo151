import turtle
import time
turtle.delay(0)
turtle.speed(0)
turtle.hideturtle()
heading = 90
turtle.seth(heading)
turtle.tracer(0)
turtle.penup()

kochSettings = {
    "level": 0,
    "branch":0,
    "size": 0,
    "colour1": [0, 0, 0],
    "colour2": [0, 0, 0],
    "inverse": ""
}

#get input from user
kochSettings["level"] = int(input("How many levels do you want the Koch Snowflake to have (max 4)? ").strip())
kochSettings["branch"] = int(input("How many levels do you want the Koch Snowflakes to have (max 4)? ").strip())
kochSettings["size"] = int(input("How big do you want the snowflakes to be? ").strip())
kochSettings["colour1"] = input("What colour do you want for the Koch Snowflake? ").strip().lower()
kochSettings["colour2"] = input("What colour do you want for the background? ").strip().lower()
kochSettings["inverse"] = input("Do you want to reverse the Koch snowflakes (y/n)? ").lower().strip()

global linesDrawn
linesDrawn = 0
start = time.time()
global current
current = 1

# function used to check if the snowflake is inversed or not
def checkInverse(num):
    # if the inverted setting is on, then reverse the turning of the turtle which is how to create the inversed snowflake (aka Mitsubishi Logo)
    return num if kochSettings["inverse"] == "n" else -num


# kochLine draws a singular side of a Koch snowflake. 
def kochLine(level, length):
    #base case: draws a singular line and count
    if level == 1:
        global linesDrawn
        turtle.forward(length)
        linesDrawn += 1
    else:
        #creates a "curve" on the side of the triangle
        kochLine(level-1, length/3)
        turtle.left(60)
        kochLine(level-1, length/3)
        turtle.right(120)
        kochLine(level-1, length/3)
        turtle.left(60)
        kochLine(level-1, length/3)
    
# recursive function that draws a full koch snowflake, with it surrounded by 
def kochSnowflake(level, length, colour, tile):
    turtle.fillcolor(colour)
    turtle.begin_fill()
    kochLine(level, length)
    # after finishing drawing a line of the triangle, checks the level. If not the base case, then draws an additional snowflake.
    # the begin_fill and end_fill are to try to colour as much of the triangle as possible since the way fill works doens't really 
    # work well with recursive functions.
    if tile > 0:
        turtle.end_fill()
        turtle.begin_fill()
        turtle.left(60)
        kochSnowflake(level, length, colour, tile-1)
        turtle.right(60)
        turtle.end_fill()
        turtle.begin_fill()
    turtle.right(checkInverse(120))
    kochLine(level, length)
    if tile > 0:
        turtle.end_fill()
        turtle.begin_fill()
        turtle.left(60)
        kochSnowflake(level, length, colour, tile-1)
        turtle.right(60)
        turtle.end_fill()
        turtle.begin_fill()
    turtle.right(checkInverse(120))
    kochLine(level, length)
    if tile > 0:
        turtle.end_fill()
        turtle.begin_fill()
        turtle.left(60)
        kochSnowflake(level, length, colour, tile-1)
        turtle.right(60)
        turtle.end_fill()
        turtle.begin_fill()
    turtle.right(checkInverse(120))
    turtle.end_fill()


turtle.goto(0, 0)
turtle.seth(heading)
turtle.forward(kochSettings["size"]/2)
turtle.right(150)
turtle.pendown()
turtle.bgcolor(kochSettings["colour2"])
turtle.pencolor(kochSettings["colour1"])

# loop to create a spinning animation
while True:
    turtle.clear()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.seth(heading)
    #to center the snowflake based on the size
    turtle.forward(kochSettings["size"]/2)
    turtle.right(checkInverse(150))
    turtle.pendown()
    kochSnowflake(kochSettings["level"], kochSettings["size"], kochSettings["colour1"], kochSettings["branch"])
    turtle.update()
    print(f"\rTotal lines drawn: {linesDrawn} | Lines Drawn per Second: {linesDrawn/(time.time()-start):.5f}", end=" ")
    heading += 1
turtle.done()