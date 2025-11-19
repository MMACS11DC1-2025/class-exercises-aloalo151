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
        if x/height < 1/7:
            colours = (255, imgg, imgb)
        if x/height < 2/7:
            colours = (255, 125, imgb)
        if x/height < 3/7:
            colours = (255, 255, imgb)
        if x/height < 4/7:
            colours = (imgr, 255, imgb)
        if x/height < 5/7:
            colours = (imgr, imgg, 255)
        if x/height < 6/7:
            colours = (75, imgg, 130)
        if x/height < 7/7:
            colours = (255, imgg, 255)
        image_output.putpixel(xy, colours)
        
image_output.save("output.jpg")
image_output.show()

        
