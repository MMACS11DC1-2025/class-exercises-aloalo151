from PIL import Image

image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()

image_output = Image.open("5.1/kid-green.jpg")

width = image_output.width
height = image_output.height

imgr = 0
imgg = 0
imgb = 0

for i in range(width):
    for x in range(height):
        imgr = image_green[i, x][0]
        imgg = image_green[i, x][1]
        imgb = image_green[i, x][2]
        xy = (i, x)
        image_output.putpixel(xy, (255-imgr, 255-imgg, 255-imgb))
        
image_output.save("output.jpg")
image_output.show()

        
