"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
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
global likeHigh
likeHigh = [0, ""]
likeTemp = 0
simi = []
global sentence1
sentence1 = ""
global sentence2
sentence2 = "You are most similar to "
global name
name = ""
global nameID
nameID = 0
global mode 
mode = 0
global traits
traits = []
global simiPpl
simiPpl = []
# put bigData in a list
# for each line in the response file, strip the \n at the end of the line and split the line into a list, 
# which is put in a bigger list  
for line in file:
    bigData.append(line.strip("\n ").split(","))

# ask the user for the person they want to compare
def init():
    global name
    global nameID
    global mode
    name = input("Please enter your full name: ").lower().strip(";., ")
    for person in range(len(bigData)):
        if name == bigData[person][1].lower():
            nameID = int(bigData[person][0])
    if nameID == 0:
        print("Please try again.")
        init()
    mode = int(input("Do you want to find people with a same specific interest or someone with overall similar interest? Enter 1 for the for and 2 for the latter. "))

# ask what traits the users have in mind
# ask what the user want through a number system and convert the input into a list
def inputTrait():
    global traits
    print("Please select the traits that you want by listing the numbers correspondent to each trait, seperated by a comma")
    print("ie. for music genre and animal, enter \"6, 2\"")
    print("1 for favourite number")
    print("2 for favourite animal")
    print("3 for favourite subject in school")
    print("4 for favourite sport to play")
    print("5 for favourite sport to watch")
    print("6 for favourite music genre")
    print("7 for favourite movie genre")
    print("8 for favourite fast food nearby")
    traits = input("Enter your selection: ").split(",")
    for trait in range(len(traits)):
        traits[trait] = traits[trait].replace(" ", "")
        traits[trait] = int(traits[trait])

# goes through the list of people and find the people with the same interest using the input from the user.
# goes through each person in the list and comparing their traits to the user's using the index inputed by the user
def findTraits():
    global traits
    global simiPpl
    for person in range(len(bigData)): 
        if bigData[person][0] != str(nameID):
            quota = 0
            for trait in range(len(traits)):
                if bigData[person][trait+1] == bigData[nameID][trait+1]:
                    quota += 1
            if quota == len(traits):
                simiPpl.append(bigData[person][1])
                
# make sentence
def constructSentence1():
    global sentence1
    for person in range(len(simiPpl)):
        if person == len(simiPpl)-1:
            sentence1 = f"{sentence1}and {simiPpl[person]}"
        else:
            sentence1 = f"{sentence1}{simiPpl[person]}, "
    sentence1 = f"{sentence1} also like"
    for trait in traits:
        sentence1 = f"{sentence1} {bigData[nameID][trait+1]},"
    sentence1 = sentence1.replace(",", ".")
    print(sentence1)
                
# Find the person most alike to the user
# goes through the big list and compare each person's responses (excluding the user) to the user's
# record the number of similarities and compare it to the previous highest 
def findAlike():
    for person in range(len(bigData)):
        if bigData[person][0] != str(nameID):
            # counter for current person's amount of similarities
            likeTemp = 0
            for item in range(len(bigData[person])):
                if bigData[person][item] == bigData[nameID][item]:
                    likeTemp += 1
            # compares the current count to the previous highest
            global likeHigh
            if likeTemp > likeHigh[0]:
                likeHigh = [likeTemp, bigData[person][1], bigData[person][0], person] 
                
# find the similarities between the 2 people
# makes a list of the things the two people have in common by comparing each of the lists' correspondent items
def findAlikeItems():
    for item in range(len(bigData[int(likeHigh[2])])):
        if bigData[likeHigh[3]][item] == bigData[nameID][item]:
            simi.append(bigData[likeHigh[3]][item])

# construct the final sentence
# go through the list of similarities and add them to the sentence. At the last item, end the sentence
def ConstructSentence2():
    global sentence2
    sentence2 = f"{sentence2}{likeHigh[1]}. You both like"
    for like in range(len(simi)):
        if like == len(simi)-1:
            sentence2 = f"{sentence2} and {simi[like]}!"
        else:
            sentence2 = f"{sentence2} {simi[like]},"
    print(sentence2)


if __name__ == "__main__":
    init()
    if mode == 1:
        inputTrait()
        findTraits()
        constructSentence1()
    elif mode == 2:
        findAlike()
        findAlikeItems()
        ConstructSentence2()