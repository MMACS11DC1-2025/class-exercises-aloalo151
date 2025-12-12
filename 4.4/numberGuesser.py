import random

correct = False
mystery = random.randint(1, 100)
count = 0
while not correct:
    guess = int(input("Guess the number: "))
    if guess == mystery:
        break
    print("Too high, try again" if guess > mystery else "Too low, try again")
    count += 1
print(f"You won with {count} guesses!")