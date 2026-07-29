# Student Grade Calculator

total = 0

for i in range(1, 6):
    mark = int(input(f"Enter mark {i}: "))
    total += mark

average = total / 5

print("\nTotal Marks:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 40:
    print("Grade: D")
else:
    print("Grade: F")
    