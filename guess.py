import random

number = random.randint(1, 20)

print("🎯 Guess the number between 1 and 20")

while True:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("⬆️ Too low!")

    elif guess > number:
        print("⬇️ Too high!")

    else:
        print("🎉 Correct!")
        break