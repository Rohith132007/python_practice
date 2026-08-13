score = 0

print("🧠 MINI QUIZ")
print()

answer = input("1. What is the capital of India? ")

if answer.lower() == "delhi":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong!")

answer = input("2. How many days are there in a week? ")

if answer == "7":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong!")

answer = input("3. Which language are we learning? ")

if answer.lower() == "python":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong!")

print()
print("Your score:", score, "/ 3")