import random

print("🎲 Dice Rolling Game")

roll = input("Press Enter to roll the dice...")

dice = random.randint(1, 6)

print("You rolled:", dice)

if dice == 6:
    print("🔥 Great! You got 6!")
elif dice == 1:
    print("😅 Oops! You got 1.")
else:
    print("👍 Nice roll!")