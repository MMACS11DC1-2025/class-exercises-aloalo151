import turtle
amt = int(input("How big (recommended <500)? "))
shape1 = turtle.Turtle()
shape2 = turtle.Turtle()
shape3 = turtle.Turtle()
shape4 = turtle.Turtle()
shape2.left(180)
shape3.right(90)
shape4.left(90)
inv = input("Inverted (Y/N)? ").lower()
colour = input("Colour? ")
if colour.lower() != "pride":
    shape1.color(colour)
    shape2.color(colour)
    shape3.color(colour)
    shape4.color(colour)
if inv == "y":
    intX = 0
    intY = 0
    x = 900
    y = 450
elif inv == "n": 
    intX = 900
    intY = 450
    x = 1800
    y = 900
elif inv == "bo":
    intX = 900
    intY = 450
    x = 1800
    y = 900

def lines1():
    global line1
    shape1.penup()
    shape1.goto(pointsX1[line1])
    shape1.pendown()
    shape1.goto(pointsY1[line1])
    line1 += 1
    
def lines2():
    global line2
    shape2.penup()
    shape2.goto(pointsX2[line2])
    shape2.pendown()
    shape2.goto(pointsY2[line2])
    line2 += 1
    
def lines3():
    global line3
    shape3.penup()
    shape3.goto(pointsX3[line3])
    shape3.pendown()
    shape3.goto(pointsY3[line3])
    line3 += 1
    
def lines4():
    global line4
    shape4.penup()
    shape4.goto(pointsX4[line4])
    shape4.pendown()
    shape4.goto(pointsY4[line4])
    line4 += 1
    
for i in range(len(inv)):
    turtle.delay(0)
    shape1.speed(0)
    shape1.penup()
    shape1.goto(-intX,-intY)
    shape1.pendown()
    pointsX1 = []
    pointsY1 = []
    shape2.speed(0)
    shape2.penup()
    shape2.goto(intX, intY)
    shape2.pendown()
    # shape2.left(180)
    pointsX2 = []
    pointsY2 = []
    shape3.speed(0)
    shape3.penup()
    shape3.goto(-intX, intY)
    shape3.pendown()
    # shape3.right(90)
    pointsX3 = []
    pointsY3 = []
    shape4.speed(0)
    shape4.penup()
    shape4.goto(intX, -intY)
    shape4.pendown()
    # shape4.left(90)
    pointsX4 = []
    pointsY4 = []
    global line1
    line1 = 0
    global line2
    line2 = 0
    global line3
    line3 = 0
    global line4
    line4 = 0
    offset = 0
    shape1.hideturtle()
    shape2.hideturtle()
    shape3.hideturtle()
    shape4.hideturtle()
    
    while(offset < amt):
        shape1.forward(x/amt)
        pointsX1.append(shape1.position())
        shape2.forward(x/amt)
        pointsX2.append(shape2.position())
        shape3.forward(y/amt)
        pointsY3.append(shape3.position())
        shape4.forward(y/amt)
        pointsY4.append(shape4.position())
        offset += 1
    shape1.goto(-intX,-intY)
    shape1.left(90)
    shape2.goto(intX, intY)
    shape2.left(90)
    shape3.goto(-intX, intY)
    shape3.left(90)
    shape4.goto(intX, -intY)
    shape4.left(90)
    offset = 0
    while(offset < amt):
        shape1.forward(y/amt)
        pointsY1.append(shape1.position())
        shape2.forward(y/amt)
        pointsY2.append(shape2.position())
        shape3.forward(x/amt)
        pointsX3.append(shape3.position())
        shape4.forward(x/amt)
        pointsX4.append(shape4.position())
        offset += 1
    pointsY1.reverse()
    pointsY2.reverse()
    pointsY3.reverse()
    pointsY4.reverse()



    while line1 < len(pointsX1): 
        if colour.lower() == "pride":
            if line1/len(pointsX1) < 1/7:
                shape1.pencolor("red")
                shape2.pencolor("red")
                shape3.pencolor("red")
                shape4.pencolor("red")
            elif line1/len(pointsX1) < 2/7:
                shape1.pencolor("orange")
                shape2.pencolor("orange")
                shape3.pencolor("orange")
                shape4.pencolor("orange")
            elif line1/len(pointsX1) < 3/7:
                shape1.pencolor("yellow")
                shape2.pencolor("yellow")
                shape3.pencolor("yellow")
                shape4.pencolor("yellow")
            elif line1/len(pointsX1) < 4/7:
                shape1.pencolor("green")
                shape2.pencolor("green")
                shape3.pencolor("green")
                shape4.pencolor("green")
            elif line1/len(pointsX1) < 5/7:
                shape1.pencolor("blue")
                shape2.pencolor("blue")
                shape3.pencolor("blue")
                shape4.pencolor("blue")
            elif line1/len(pointsX1) < 6/7:
                shape1.pencolor("indigo")
                shape2.pencolor("indigo")
                shape3.pencolor("indigo")
                shape4.pencolor("indigo")
            elif line1/len(pointsX1) < 7/7:
                shape1.pencolor("violet")
                shape2.pencolor("violet")
                shape3.pencolor("violet")
                shape4.pencolor("violet")
        lines1()
        lines2()
        lines3()
        lines4()

    if inv == "bo":
        intX = 0
        intY = 0
        x = 900
        y = 450
        shape1.right(90)
        shape2.right(90)
        shape3.right(90)
        shape4.right(90)

    
    
    


        
turtle.done()