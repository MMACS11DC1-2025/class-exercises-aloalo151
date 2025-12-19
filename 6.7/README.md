# MORSE-IMAGES-TRANSLATEINATOR
### by Nguyen Doan

<img src="morse_images/morse5.png" height="140" width="1500">

## Project Description: 
The Translateinator will take images of morse code messages and translate them into morse code text by detecting different "blobs" of characters and categorizes  them, which is then translated to English and sorted alphabetically<br>
Inspired and uses some processes in Optical Character Recognition, which is commonly used to process images into text files.

## Process:
> ### Initialization
To help with processing the image, the program get ready by binarizing the image
and making a 2D array copy of the image's pixels:
```
for y in range(height):
        imgLabels.append([])
        for x in range(width):
            imgLabels[y].append("")
```

> ### Labeling
Labeling is the process of giving each pixel a label correspondent with its "shape", allowing the grouping of pixels and formation of the individual characters<br>
To label, we use a recursive funtion that, after a successful label attempt, will label the pixels surrounding itself. 
```
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
```
The true or false that the function returns tells the program if a new "shape" was discovered 
```
if labelPixel(img, x, y, labelNum, imgLabels, width, height):
    labelNum += 1
```
<img src="readmeExample1.png" height="140" width="500"><br>
*fig. 1: a visualization of the labeling system, with each shape having a different colour. Ignore the first two being similar since this image was produced with random colours assigned*

> ### Identifying
After each shape is labeled, the program goes through each of those labels and identify each shape as a ".", "-", "/", or " "<br>
By getting the extremes of a shape, we can identify it by getting the angle of the line directly across the shape using arctan:<br><br>
<img src="readmeExample2.png" height="200" width="500"><br>
*fig. 2: by using the shape's height and width, you can calculate the angle of the diagonal line created from the extremes of the shape and identify it.*<br>

All of these characters are compiled into a string containing all of the morse code from the image, with spaces denoting the different "letters"

> ### Translating
By spliting the string into a list, we can then compare every set of morse and translate all into English using a dictionary. The sentence is reconstructed and returned. The output is then added to a list of messages.
```
morseList = []
for i in range(1, 11):
    morseList.append(translateMorseImage(f"6.7/morse_images/morse{i}.png"))
```

> ### Sorting & Searching
After the list is completed, the messages are sorted alphabetically through selection sort. <br>
A binary searching program is made, which takes a message as an input and returns the image associated with that message. It returns nothing if the program can't find a match.
```
message = input(("Enter the message: "))
        low = 0
        high = len(morseList)-1
        found = False
        while low < high:
            middle = int((low+high)/2)
            if morseList[middle][0] == message:
                print(f"morse{middle+1}")
                found = True
                break
            elif compareString(morseList[middle][0], message) == morseList[middle][0]:
                high = middle-1
            else:
                low = middle+1
        if not found:
            print("The message does not have an image associated with it")
```
<img src="readmeExample3.png" height="200" width="1500"><br>
*fig. 3: an example of using the binary search function*<br>

*Note: I didn't know that strings could be compared alphabetically using < and >, which resulted me in creating multiple functions to help sort the strings, like the compareString() function seen above.*

## Testing:
With every major developement in the code, some testing is done to ensure that the code is working as intended.<br>
1. After developing the labeling system, the images were modified to have a different colour based on their label, as shown in fig. 1. This helped visualizing the different groupings and showed any errors. 
2. During the time when the translating into morse system was made, I was only testing with one message that started with a dot and my code only ended up working wit messages starting with a dot. Ashar help pointed out this problem when he made a message starting with a dash instead, which allowed me to solve the problem early on.
3. After the entire system was done, morse messages outside of the prefered source were tested with the program. They did not work due to the difference in the height and width of their characters, but the ones that was from the source worked flawlessly.

## Performance
Each major process is time to test their performance and effciency. Here's the full list from shortest time taken to longest time taken:
1. Translating into English: This process is quick and easy since it's just comparing strings to strings
2. Labeling every pixel: This only required the program to go through every pixel once, so it's not too bad
3. Initilization: This took longer since techinally the program had to run through every pixel twice (kinda), when creating the copy list and when binarizing the image
4. Translating every labels into morse: This have the program loop through every instances of a label (one for every pixel) once for every label (the amount of characters detected). This process took the longest time purely because of that reason. I could have tried to optimize it, but that would require a much more complex translating system and the time taken is still quite insigificant.<br><br>
<img src="readmeExample4.png" width = "800"><br>
*fig. 4: An example run time report. Note that the last process was way to short to make a significant impact on time.*

## Challenges:
This was a very challenging problem that I decided to tackle, and along the way I had a multitude of problem and issues
1. How to label: I had some inspiration from connected-component labeling, which does use the same process to group elements together, but I struggled to apply that to Python
2. Labeling consistency: Since PNGs are weird, each character had like 7 shades of colour. This was somewhat solved with binarizing the image.
3. Identifying characters: Since my program basically returns a list of pixel positions with the label, I had some issues about how to identify each one of them. Brendan suggested that using trig to help caterogize the characters and that method proved to be effective. "." were also a problem since they were the most inconsistent because of their small size, but having them as the default case when everything fails works.
4. Spaces: Finding spaces between different words was an issue since my labelling system is not the best suited for that purpose since the spaces is in the whitespace, which is all the same label. I finally decided to detect the space between words by using the distance between the first two characters as a threshold for distances to be considered a space. However, this system fails if the first letter is an E or a T, since the first distance detected will be a space and ruin the rest of the message. This is why there is a specific countermeasure against this specific case.
5. Sorting: Since my functions return a string instead of a number, comparing them for the sorting and searching process was gonna be more difficult. I made two functions to assist with this process, ```compareString()``` and ```searchAlphabet()```, with the former using the latter to find corresponding letter from two strings' "value" and compare them. This was all before I learned of the fact than you can compare strings with < and > comparators.<br><br>
<img src="readmeExample5.png"><br>
*fig. 5: all of this was <b>avoidable<b>*