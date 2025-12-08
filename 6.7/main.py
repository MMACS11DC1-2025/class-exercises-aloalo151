'''
Morse Code Reader:
Go through a picture of a morse code message, identify the dots and lines, then translate the message into English. Sort by amount of words in each message.
'''

from PIL import Image
import random

''' 
Pseudocode:

image list/array = []

for pixel in width:
    imageList.append([])
    for pixel in height
        imageList[pixel].append(not_labeled)


for pixel in width
    for pixel in height
        if pixel is not labeled
            check pixel (function)
            if pixel is foreground/black
                label as black
                check surrounding pixels
            else lable as white
    '''
imgLabels = []
labelNum = 1

img = Image.open("6.7/morse_images/morse1.png").load()
imgOutput = Image.open("6.7/morse_images/morse1.png")
width, height = imgOutput.size

for y in range(height):
    imgLabels.append([])
    for x in range(width):
        imgLabels[y].append("")
        
for y in range(height):
    for x in range(width):
        if img[x, y] == (249, 250, 251, 255):
            imgOutput.putpixel([x, y], (255, 255, 255, 255))
        else:
            imgOutput.putpixel([x, y], (0, 0, 0, 0))
        
def labelPixel(x, y, label):
    if imgLabels[y][x] == "":
        r, g, b, a = img[x, y]
        if r<100 and g<100 and b<100:
            imgLabels[y][x] = label
            for x_pos in range(x-1, x+2):
                for y_pos in range(y-1, y+2):
                    if 0 <= x_pos <= width and 0 <= y_pos <= height:
                        labelPixel(x_pos, y_pos, label)
            return True
        else: 
            imgLabels[y][x] = 0
            return False
    else:
        return False

for x in range(width):
    for y in range(height):
        if labelPixel(x, y, labelNum):
            labelNum += 1
                   
label1 = []
for i in range(1, labelNum):
    colour = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
    for y in range(height):
        for x in range(width):
            if imgLabels[y][x] == i:
                imgOutput.putpixel([x, y], (colour))
            


# for y in range(height):
#     for x in range(width):
#         if imgLabels[y][x] != 0:
#             imgOutput.putpixel([x, y], (imgLabels[y][x], 0, 0))
            
# for y in range(height):
#     print(imgLabels[y])
imgOutput.save("image.png")
print(labelNum)