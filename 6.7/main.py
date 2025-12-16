'''
Morse Code Reader:
Go through a picture of a morse code message, identify the dots and lines, then translate the message into English. Sort by amount of words in each message.
'''

from PIL import Image
import time
import math

morseDict = {
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
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
    "/": " ", 
    "-....-": "-"
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
    
for each pixel:
    label them
    if labeling successful, increase label

'''
def translateMorseImage(imageName):
    timeStart = time.time()
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
    timeEnd = time.time()
    timeImgLabel = timeEnd - timeStart
     
    #binarize the image to assist in processing   
    timeStart = time.time()    
    for y in range(height):
        for x in range(width):
            if img[x, y] <= (200, 200, 200, 200):
                imgOutput.putpixel([x, y], (255, 255, 255, 255))
            else:
                imgOutput.putpixel([x, y], (0, 0, 0, 0))
    timeEnd = time.time()
    timeBinarize = timeEnd - timeStart

    #labels each pixel in the image with a number
    #after every successful label, increases the label number
    timeStart = time.time()
    for x in range(width):
        for y in range(height):
            if labelPixel(img, x, y, labelNum, imgLabels, width, height):
                labelNum += 1
    timeEnd = time.time()
    timeLabel = timeEnd - timeStart
    '''
    for each labeled shapes:
        add every pixels with the label into a seperate list
        looks through every pixel and compares it to the smallest x value, smallest y value, biggest x value, biggest y value, to get the extremes of the shape
        if this is the second shape, set the distance from it to the first one as "notSpace"
        if this is past the first shape, get the distance from this shape to the previous shape
        if current distance is more than the "notSpace", add a space
        compare the arctan of the shape's dimensions to categorize the shape and add it to the overarching string of characters
    ''' 
    timeStart = time.time()
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
    timeEnd = time.time()
    timeTranslateMorse = timeEnd - timeStart
    '''
    splits the string into a list
    translates each morse in the list into a character
    reconstructs the string with the new non-morse characters
    '''
    #splits the entire morse into a list with split
    #translate the words themselves
    timeStart = time.time()
    labelList = labelString.split(" ")
    for i in range(len(labelList)):
        for character in morseDict:
            if labelList[i] == character:
                labelList[i] = morseDict[character]

    #reconstructs the message
    message = ""
    for i in range(len(labelList)):
        message += labelList[i]
    timeEnd = time.time()
    timeTranslateEnglish = timeEnd - timeStart
    return (message, timeImgLabel, timeBinarize, timeLabel, timeTranslateMorse, timeTranslateEnglish)
'''
compares input to everything in a list
if is equal, then returns the index
else return a BIG number to put it last
'''
#function to find a character's "place" in the alphabet, to help with sorting alphabetically
def searchAlphabet(char):
    alphabet = [
    " ", "-", ",", ".", "'",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
    ]
    for i in range(len(alphabet)):
        if char == alphabet[i]:
            return i
    return 1000000000000000000000

'''
get lenght of shorter string
for each character index
    get the index of the current character from both strings
    compare them and return the smaller one
return the shorter string
'''
#function to compare two strings alphabetically
#returns shorter string if both are identical
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
        elif char2 > char1:
            return string1
    return short

morseList = []
print("")
timeStart = time.time()
for i in range(1, 11):
    morseList.append(translateMorseImage(f"6.7/morse_images/morse{i}.png"))
timeEnd = time.time()
timeTaken = timeEnd - timeStart
for pos in range(len(morseList)):
    smol = pos
    for i in range(pos+1, len(morseList)):
        if compareString(morseList[smol][0], morseList[i][0]) == morseList[i][0]:
            smol = i
    morseList[pos], morseList[smol] = morseList[smol], morseList[pos]
for i in morseList:
    print(i[0])
    print(f"Time to create ImgLabels: {i[1]}")
    print(f"Time to binarize image: {i[2]}")
    print(f"Time to label every pixel: {i[3]}")
    print(f"Time to translate all labels into morse: {i[4]}")
    print(f"Time to translate into English: {i[5]}")
    print("")
for i in range(5):
    print(morseList[i][0])
print("")
print(timeTaken)