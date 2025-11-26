file = open("2.4/responses.csv")
bigData = []
likeHigh = [0, ""]
myself = []

for line in file:
    bigData.append(line.strip("\n").split(","))
    
for person in bigData:
    if person[1] == "Nguyen Doan":
        myself = person
print(myself)
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