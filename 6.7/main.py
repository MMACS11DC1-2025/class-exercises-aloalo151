'''
Morse Code Reader:
Go through a picture of a morse code message, identify the dots and lines, then translate the message into English. Sort by amount of words in each message.
'''

from PIL import Image
import time
import math

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

# Recursive funciton that labels an unlabeled pixel and other pixels that surround it that shares the same colour
#Ignores all labeled pixels
'''
Goes through every pixel
if pixel not labeld:
    if pixel is black:
        label as label
        check surrounding pixels
        true
    else:   
        label as white
        false
false
'''
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
    
#function that fully converts an image of morse code into a string
'''
opens image
create big list
for each row/column:
    add a list to big list
    for each column/row:
        add a "" to the smaller list created above
for each pixel:
    if rgb values lesser than something
    is black
    else 
    is white

'''
def translateMorseImage(imageName):
    imgLabels = []
    labelNum = 1

    img = Image.open(imageName).load()
    imgOutput = Image.open(imageName)
    width, height = imgOutput.size

    #creates the "2D array" copy of the image to store the labels of each pixel
    for y in range(height):
        imgLabels.append([])
        for x in range(width):
            imgLabels[y].append("")
     
    #binarize the image to assist in processing       
    for y in range(height):
        for x in range(width):
            if img[x, y] == (249, 250, 251, 255):
                imgOutput.putpixel([x, y], (255, 255, 255, 255))
            else:
                imgOutput.putpixel([x, y], (0, 0, 0, 0))

    #labels each pixel in the image with a number
    #after every successful label, increases the label number
    for x in range(width):
        for y in range(height):
            if labelPixel(img, x, y, labelNum, imgLabels, width, height):
                labelNum += 1

    #variable to contained morse string
    labelString = "" 
    #threshold for the distance between each character to not be considered a space/distinguish between words (if distance > notSpace, is a space)
    notSpace = 0    
    #goes through each labeled shape and identifies it as a ".", "-", "/", or " " 
    for i in range(1, labelNum):
        labelsPixel = []
        #adds all pixels of a label into a list
        for y in range(height):
            for x in range(width):
                    if imgLabels[y][x] == i:
                        labelsPixel.append([x, y])
        prevX = (0 if i == 1 else bigX)
        bigX = labelsPixel[0][0]
        smolX = labelsPixel[0][0]
        bigY = labelsPixel[0][1]
        smolY = labelsPixel[0][1]
        
        #get the biggest and smallest values of x and y of the image
        for id in range(len(labelsPixel)):
            if labelsPixel[id][0] > bigX:
                bigX = labelsPixel[id][0]
            if labelsPixel[id][0] < smolX:
                smolX = labelsPixel[id][0]
            if labelsPixel[id][1] > bigY:
                bigY = labelsPixel[id][1]
            if labelsPixel[id][1] < smolY:
                smolY = labelsPixel[id][1]
        #get the "notSpace" distance
        if i == 2:
            notSpace = smolX - prevX
        dist = smolX - prevX

        #to fix a specific case where the first word only have a singular dot or dash
        #since the "notSpace" would be the "space" value
        if dist < notSpace*.75:
            notSpace = dist
            #go backwards in the string and inserts a space behind all the characters, since every character before would have a space in this case
            for index in range(len(labelString) -1, 0, -1):
                labelString = labelString[:index] + " " + labelString[index:]
                
        #identifies the actual character
        #if the distance is larger than "notSpace", add a space
        #if the arctan of the diagonal across the shape is in a certain range, is a slash
        #likewise, if the arctan is in a certain range, is a -
        #else, is a . 
        #. is the else since it's dimensions are quite inconsistent, despite binarizing the image. This eliminates that inconsistency
        if i > 1:
            if dist > notSpace*1.5:
                labelString += " "
        if 1.1 < math.atan((bigY-smolY)/(bigX-smolX)) < 1.23:
            labelString += "/"
        elif 0.1 < math.atan((bigY-smolY)/(bigX-smolX)) < 0.2:
            labelString += "-"
        else:
            labelString += "."       

    #splits the entire morse into a list with split
    #translate the words themselves
    labelList = labelString.split(" ")
    for i in range(len(labelList)):
        for character in morseDict:
            if labelList[i] == character:
                labelList[i] = morseDict[character]

    #reconstructs the message
    message = ""
    for i in range(len(labelList)):
        message += labelList[i]
    return message
  
def searchAlphabet(char):
    alphabet = [
    " ", "'", ",", ".",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
    ]
    for i in range(len(alphabet)):
        if char == alphabet[i]:
            return i
    return 1000000000000000000000
    
def compareString(string1, string2):
    if len(string1) > len(string2):
        length = len(string2)
        short = string2
    else:
        length = len(string1)
        short = string1
    for i in range(length):
        char1 = searchAlphabet(string1[i])
        char2 = searchAlphabet(string2[i])
        if char1 > char2:
            return string2
        elif char2 < char1:
            return string1
    return short
        
morseList = []
print("")
timeStart = time.time()
for i in range(1, 4):
    morseList.append(translateMorseImage(f"6.7/morse_images/morse{i}.png"))
timeEnd = time.time()
timeTaken = timeEnd - timeStart
for pos in range(len(morseList)):
    smol = pos
    for i in range(pos+1, len(morseList)):
        if compareString(morseList[smol], morseList[i]) == morseList[i]:
            smol = i
    morseList[pos], morseList[smol] = morseList[smol], morseList[pos]
for i in morseList:
    print(i)
print("")
print(timeTaken)