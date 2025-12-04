binary = input("Enter your binary number: ")[::-1].split(" ")
decimal = 0
numberList = []
for number in range(len(binary)):
    decimal = 0
    for digit in range(len(binary[number])):
        decimal += int(binary[number][digit])*2**digit
    numberList.append(decimal)
numberList.reverse()
for number in range(len(numberList)):
    numberList[number] = f"{str(numberList[number])}   {chr(numberList[number])}"
for stuff in numberList:
    print(stuff)