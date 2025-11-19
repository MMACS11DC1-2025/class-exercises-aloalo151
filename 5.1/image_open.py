from PIL import Image

image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()

image_output = Image.open("5.1/kid-green.jpg")

width = image_output.width
height = image_output.height

imgr = 0
imgg = 0
imgb = 0

def is_green(r, g, b):
    return True if 0<=r<=25 and 0<=g<=255 and 0<=b<=25 else False

def colour(r, g, b):
    colors = {
        "Red":[1, 0, 0], 
        "Green":[0, 1, 0],
        "Blue":[0, 0, 1], 
        "White":[1, 1, 1], 
        "Black":[0, 0, 0], 
        "Yellow":[1, 1, 0], 
        "Magenta":[1, 0, 1]
    }
    
    colorlist = [0, 0, 0]
    if 0<=r<=50:
        colorlist[0] = 0
    elif 200<=r<=255:
        colorlist[0] = 1
        
    if 0<=g<=50:
        colorlist[1] = 0
    elif 200<=g<=255:
        colorlist[1] = 1
        
    if 0<=b<=50:
        colorlist[2] = 0
    elif 150<=b<=255:
        colorlist[2] = 1
        
    for colour in colors:
        if colorlist == colors[colour]:
            return colors[colour]
    return "unknown"

for i in range(width):
    for x in range(height):
        imgr = image_green[i, x][0]
        imgg = image_green[i, x][1]
        imgb = image_green[i, x][2]
        if is_green(imgr, imgg, imgb):
            xy = (i, x)
            image_output.putpixel(xy, image_beach[i, x])
        
image_output.save("output.jpg")
image_output.show()

        
