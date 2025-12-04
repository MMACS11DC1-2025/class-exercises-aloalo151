'''
Morse Code Reader:
Go through a picture of a morse code message, identify the dots and lines, then translate the message into English. Sort by amount of words in each message.
'''

from PIL import Image

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

for x in range(width):
    imgLabels.append([])
    for y in range(height):
        imgLabels[x].append("")
        
for x in range(width):
    for y in range(height):
        if img[x, y] == (249, 250, 251, 255):
            imgOutput.putpixel([x, y], (255, 255, 255, 255))
        else:
            imgOutput.putpixel([x, y], (0, 0, 0, 0))
        
def labelPixel(x, y, label):
    if imgLabels[x][y] == "":
        r, g, b, a = img[x, y]
        if r<249 and g<250 and b<251:
            imgLabels[x][y] = label
            for x_pos in range(x-1, x+2):
                for y_pos in range(y-1, y+2):
                    if 0 <= x_pos <= width and 0 <= y_pos <= height and (x_pos != x and y_pos != y):
                        labelPixel(x_pos, y_pos, label)
            return True
        else: 
            imgLabels[x][y] = 0
            return False

for x in range(width):
    for y in range(height):
        if labelPixel(x, y, labelNum):
            labelNum += 1
print(img[0, 0] == (249, 250, 251, 255))
imgOutput.save("image.png")