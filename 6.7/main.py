'''
Morse Code Reader:
Go through a picture of a morse code message, identify the dots and lines, then translate the message into English. Sort by amount of words in each message.
'''

from PIL import Image
import random
import math

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

img = Image.open("6.7/morse_images/morse2.png").load()
imgOutput = Image.open("6.7/morse_images/morse2.png")
width, height = imgOutput.size
morseDict = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z', 
    "--..--": ",",
    ".-.-.-": ".",
    ".----.": "'"
}

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
        if r<120 and g<120 and b<120:
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

labelList = []    

notSpace = 0     
for i in range(1, labelNum):
    labelPixel = []
    for y in range(height):
        for x in range(width):
                if imgLabels[y][x] == i:
                    labelPixel.append([x, y])
    prevX = (0 if i == 1 else bigX)
    bigX = labelPixel[0][0]
    smolX = labelPixel[0][0]
    bigY = labelPixel[0][1]
    smolY = labelPixel[0][1]
    for id in range(len(labelPixel)):
        if labelPixel[id][0] > bigX:
            bigX = labelPixel[id][0]
        if labelPixel[id][0] < smolX:
            smolX = labelPixel[id][0]
        if labelPixel[id][1] > bigY:
            bigY = labelPixel[id][1]
        if labelPixel[id][1] < smolY:
            smolY = labelPixel[id][1]
    if i == 2:
        notSpace = bigX - prevX
    dist = smolX - prevX
    # print(f"bigX: {bigX}")
    # print(f"smolX: {smolX}")
    # print(f"prevX: {prevX}")
    # print(f"notSpace: {notSpace}")
    # print(f"dist: {dist}")
    # print("")
    if dist < notSpace*.75:
        notSpace = dist
        for index in range(len(labelList) -1, -1, -1):
            labelList.insert(index, " ")
    if i > 1:
        if dist > notSpace*1.5:
            labelList.append(" ")
    if 1.1 < math.atan((bigY-smolY)/(bigX-smolX)) < 1.23:
        labelList.append("/")
    elif 0.1 < math.atan((bigY-smolY)/(bigX-smolX)) < 0.2:
        labelList.append("-")
    else:
        labelList.append(".")        
                    
    


for i in range(1, labelNum):
    colour = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
    for y in range(height):
        for x in range(width):
            if imgLabels[y][x] == i:
                imgOutput.putpixel([x, y], (colour))
            


for character in range(len(labelList)):
    for letter in morseDict:
        if letter == labelList[character]:
            labelList[character] == morseDict[letter]
    
imgOutput.save("image.png")
print(labelNum)
message = ""
for i in labelList:
    message += i
print(message)