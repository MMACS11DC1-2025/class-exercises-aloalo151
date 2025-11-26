from PIL import Image
import time


def colour(r, g, b):
    colors = {
        (1, 0, 0):"Red", 
        (0, 1, 0):"Green",
        (0, 0, 1):"Blue/Purple", 
        (1, 1, 1):"White", 
        (0, 0, 0):"Black", 
        (1, 1, 0):"Yellow", 
        (1, 0, 1):"Blue/Purple"
    }
    
    colorlist = [0, 0, 0]
    if 150<=r<=255:
        colorlist[0] = 1
        
    if 100<=g<=255:
        colorlist[1] = 1
        
    if 100<=b<=255:
        colorlist[2] = 1

    for colour in colors:
        if tuple(colorlist) == colour:
            return colors[colour]
    return "unknown"

image_jelly = Image.open("5.4/jelly_beans.jpg").load()
image_output = Image.open("5.4/jelly_beans.jpg")

width = image_output.width
height = image_output.height
colours = {
    "Red":0, 
    "Yellow":0, 
    "Blue/Purple":0, 
    "Green":0
    }

timer = time.time()

# for x in range(width):
#     for y in range(height):
#         r, g, b = image_jelly[x,y]
#         for i in colours:
#             if colour(r, g, b) == i:
#                 colours[i] += 1
timeTaken = time.time() - timer            
for i in colours:
    colours[i] = f"{round(colours[i]/(width*height)*100, 2)}%"

print(colours)
print(timeTaken)
            
            
# image_output.save("output.png")
# image_output.show()