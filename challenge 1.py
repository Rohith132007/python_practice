import random

number = random.randint(1, 100)
guesses = []

print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))

    if guess < 1 or guess > 100:
        print("OUT OF BOUNDS")
        continue

    guesses.append(guess)

    if guess == number:
        print(f"Correct! You guessed the number in {len(guesses)} guesses.")
        break

    if len(guesses) == 1:
        if abs(number - guess) <= 10:
            print("WARM!")
        else:
            print("COLD!")
    else:
        if abs(number - guess) < abs(number - guesses[-2]):
            print("WARMER!")
        else:
            print("COLDER!")