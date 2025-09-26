file = open("2.4/responses.csv")
bigData = []
lineCounter = 0
likeHigh = [0, ""]
for line in file:
    bigData.append(line.split(","))
    bigData[lineCounter][9] = bigData[lineCounter][9].strip("\n")
    lineCounter += 1
# for item in bigData:
#     print(item)
# print(bigData)
# for person in bigData:
#     likeTemp = 0
#     for item in person:
#         if item == bigData[19][bigData.index(item)]:
#             likeTemp += 1
#     if likeTemp > likeHigh[0]:
#         likeHigh = [likeTemp, person[1]]
# print(likeHigh)        