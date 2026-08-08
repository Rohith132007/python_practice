score = 0

questions = [
    ["What is the capital of India?", "delhi"],
    ["How many days are there in a week?", "7"],
    ["Which language are we learning?", "python"]
]

for question, answer in questions:
    user = input(question + " ")

    if user.lower() == answer:
        print("Correct! ✅")
        score += 1
    else:
        print("Wrong! ❌")

print("\nYour score:", score, "/", len(questions))

if score == len(questions):
    print("🏆 Perfect Score!")
elif score >= 2:
    print("👍 Good job!")
else:
    print("📚 Keep practicing!")