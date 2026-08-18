import random

print("🪙 COIN TOSS GAME")

choice = input("Choose Heads or Tails: ").lower()

coin = random.choice(["heads", "tails"])

print("Coin result:", coin)

if choice == coin:
    print("🎉 You win!")
else:
    print("❌ You lose!")