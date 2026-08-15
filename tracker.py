total = 0

print("💰 EXPENSE TRACKER")

for i in range(3):
    expense = float(input("Enter expense: ₹"))
    total += expense

print("----------------")
print("Total expense: ₹", total)

if total > 1000:
    print("⚠️ You spent a lot!")
else:
    print("👍 Good spending!")