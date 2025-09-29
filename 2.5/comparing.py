"""
Create a program that uses comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You may use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
file = open("2.4/responses.csv")
bigData = []
lineCounter = 0
likeHigh = [0, ""]
simi = []
sentence = "You are most similar to "
# put bigData in a list
for line in file:
    bigData.append(line.split(","))
    bigData[lineCounter][9] = bigData[lineCounter][9].strip("\n")
    lineCounter += 1
    
# Find the person most alike to me
for person in bigData:
    if person[0] != "19":
        likeTemp = 0
        current = 0
        for item in person:
            if item == bigData[19][current]:
                likeTemp += 1
            current += 1
        if likeTemp > likeHigh[0]:
            likeHigh = [likeTemp, person[1], person[0]]
current = 0       

# find the similarities between the 2 people
for item in bigData[int(likeHigh[2])]:
    if item == bigData[19][current]:
        simi.append(item)
    current += 1

# construct the final sentence
sentence = f"{sentence}{likeHigh[1]}. You both like"
counter = 0
for like in simi:
    if int(counter) == int(len(simi)-1):
        sentence = f"{sentence} and {like.lower()}!"
    else:
        sentence = f"{sentence} {like.lower()},"
    counter += 1
print(sentence)