import math

hexa = (input("Enter your hexaDecimal number: ")).split(" ")
for number in range(len(hexa)):
    hexa[number] = list(hexa[number])
hexaDict = {
    "A": "10",
    "B": "11",
    "C": "12", 
    "D": "13",
    "E": "14",
    "F": "15",
    "a": "10",
    "b": "11",
    "c": "12", 
    "d": "13",
    "e": "14",
    "f": "15"
}
decimal = []
binary = []
oneBigBinaryNumber = ""
for number in range(len(hexa)):
    num = 0
    for digit in range(len(hexa[number])):
        if hexa[number][digit] in hexaDict:
            hexa[number][digit] = hexaDict.get(hexa[number][digit])
        num += int(hexa[number][digit])*16**(len(hexa[number])-1-digit)
    decimal.append(num)
print(decimal)

for number in range(len(decimal)):
    num = ""
    decValue = decimal[number]
    for i in range(8):
        if 2**(7-i) <= decValue:
            decValue -= 2**(7-i)
            num = num + "1"
        else:
            num = num + "0"
    binary.append(num)

for num in binary:
    oneBigBinaryNumber = oneBigBinaryNumber + num + " "
print(oneBigBinaryNumber)
