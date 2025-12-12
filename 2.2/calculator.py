"""
Machines are good at crunching numbers - faster and more accurately than most 
humans! Create a small program that calculates something useful to you 
(making you smile is useful). It should take user input, at use at least one of the 
number operators we saw in class: + / * . You may modify one of your previous 
exercises to include calculations, if you wish.

Remember to design your algorithm in English first, then translate it to Python 
code. Test as you go!
"""

print("Please enter your calculation:")
calculation = input().split()
answer = 0
for i in range(3):
    calculation[i] = calculation[i].strip()
    if i == 0 or i == 2:
        calculation[i] = float(calculation[i])
match calculation[1]:
	case "+":
		answer = calculation[0]+calculation[2]
	case "-":
		answer = calculation[0]-calculation[2]
	case "x":
		answer = calculation[0]*calculation[2]
	case "":
		answer = calculation[0]*calculation[2]
	case "/":
		answer = calculation[0]/calculation[2]
	case "^":
		answer = calculation[0]**calculation[2]
print(f"Your answer is {answer}")