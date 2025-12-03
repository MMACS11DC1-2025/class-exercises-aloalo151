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

img = Image.open("6.7/morse_images/morse1.png")
width, height = img.size
img = img.load()

for x in range(width):
    imgLabels.append([])
    for y in range(height):
        imgLabels[x].append("")
        
def labelPixel(x, y, label):
    if imgLabels[x][y] == "":
        r, g, b = imgLabels[x, y]
        if r<25 and g<25 and b<25:
            imgLabels[x][y] = label
            return True
        else: 
            imgLabels[x][y] = 0
            return False

