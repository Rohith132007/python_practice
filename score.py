score = 0

print("Python Quiz!")

answer = input("What is the output of 2 + 3? ")

if answer == "5":
    print("Correct! ")
    score += 1
else:
    print("Wrong! ")

answer = input("Which keyword is used to define a function? ")

if answer == "def":
    print("Correct! ")
    score += 1
else:
    print("Wrong! ")

print("Your score:", score, "/ 2")