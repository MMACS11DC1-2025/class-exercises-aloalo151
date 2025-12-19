import turtle as t

turtle = t.Turtle()
turtle.hideturtle()

def draw_tree(level, branch_length):
    if level > 0:
        turtle.forward(branch_length)
        
        turtle.left(40)
        draw_tree(level-1, branch_length/1.61)
        
        turtle.right(40)
        draw_tree(level-1, branch_length/1.61)
        
        turtle.right(40)
        draw_tree(level-1, branch_length/1.61)
        
        turtle.left(40)
        turtle.back(branch_length)
    else:
        turtle.color("green")
        turtle.stamp()
        turtle.color("brown")
        
turtle.speed(0)
turtle.penup()
turtle.goto(0,-180)
turtle.left(90)
turtle.pendown()

# Setup drawing
turtle.color("brown")
turtle.width(3)
turtle.shape("turtle")
turtle.shapesize(50, 10, 0)

#Draw a tree using a recursive function
draw_tree(5, 120)

t.done()
    