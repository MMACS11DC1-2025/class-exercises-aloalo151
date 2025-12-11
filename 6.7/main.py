'''
Morse Code Reader:
Go through a picture of a morse code message, identify the dots and lines, then translate the message into English. Sort by amount of words in each message.
'''

from PIL import Image
import time
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
    ".----.": "'",
    "/": " "
}

def labelPixel(img, x, y, label, imgLabels, width, height):
    if imgLabels[y][x] == "":
        r, g, b, a = img[x, y]
        if r<120 and g<120 and b<120:
            imgLabels[y][x] = label
            for x_pos in range(x-1, x+2):
                for y_pos in range(y-1, y+2):
                    if 0 <= x_pos <= width and 0 <= y_pos <= height:
                        labelPixel(img, x_pos, y_pos, label, imgLabels, width, height)
            return True
        else: 
            imgLabels[y][x] = 0
            return False
    else:
        return False
def translateMorseImage(imageName):
    imgLabels = []
    labelNum = 1

    img = Image.open(imageName).load()
    imgOutput = Image.open(imageName)
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

    for x in range(width):
        for y in range(height):
            if labelPixel(img, x, y, labelNum, imgLabels, width, height):
                labelNum += 1

    labelString = ""   

    notSpace = 0     
    for i in range(1, labelNum):
        labelsPixel = []
        for y in range(height):
            for x in range(width):
                    if imgLabels[y][x] == i:
                        labelsPixel.append([x, y])
        prevX = (0 if i == 1 else bigX)
        bigX = labelsPixel[0][0]
        smolX = labelsPixel[0][0]
        bigY = labelsPixel[0][1]
        smolY = labelsPixel[0][1]
        for id in range(len(labelsPixel)):
            if labelsPixel[id][0] > bigX:
                bigX = labelsPixel[id][0]
            if labelsPixel[id][0] < smolX:
                smolX = labelsPixel[id][0]
            if labelsPixel[id][1] > bigY:
                bigY = labelsPixel[id][1]
            if labelsPixel[id][1] < smolY:
                smolY = labelsPixel[id][1]
        if i == 2:
            notSpace = smolX - prevX
        dist = smolX - prevX
        # print(f"bigX: {bigX}")
        # print(f"smolX: {smolX}")
        # print(f"prevX: {prevX}")
        # print(f"notSpace: {notSpace}")
        # print(f"dist: {dist}")
        # print("")
        if dist < notSpace*.75:
            notSpace = dist
            for index in range(len(labelString) -1, 0, -1):
                labelString = labelString[:index] + " " + labelString[index:]
        if i > 1:
            if dist > notSpace*1.5:
                labelString += " "
        if 1.1 < math.atan((bigY-smolY)/(bigX-smolX)) < 1.23:
            labelString += "/"
        elif 0.1 < math.atan((bigY-smolY)/(bigX-smolX)) < 0.2:
            labelString += "-"
        else:
            labelString += "."       
    # print(labelString)
    # for i in range(1, labelNum):
    #     colour = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
    #     for y in range(height):
    #         for x in range(width):
    #             if imgLabels[y][x] == i:
    #                 imgOutput.putpixel([x, y], (colour)) 
    # imgOutput.save("image.png")
    # print(labelNum)
    # message = ""
    # for i in labelList:
    #     message += i

    labelList = labelString.split(" ")
    for i in range(len(labelList)):
        for character in morseDict:
            if labelList[i] == character:
                labelList[i] = morseDict[character]

    message = ""
    for i in range(len(labelList)):
        message += labelList[i]
    return message
    
# print(translateMorseImage("6.7/morse_images/morse4.png"))
morseList = []
print("")
timeStart = time.time()
for i in range(1, 4):
    morseList.append(translateMorseImage(f"6.7/morse_images/morse{i}.png"))
timeEnd = time.time()
timeTaken = timeEnd - timeStart
morseList.sort()
for i in morseList:
    print(i)
print("")
print(timeTaken)