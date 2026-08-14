import random

password = random.randint(1000, 9999)

print("🔐 Guess the 4-digit password!")

while True:
    guess = int(input("Enter your guess: "))

    if guess == password:
        print("🎉 Correct! You cracked the password!")
        break

    elif guess < password:
        print("Too small! Try a bigger number.")

    else:
        print("Too big! Try a smaller number.")