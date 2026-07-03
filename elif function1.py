print("=== Mini Adventure Game ===")
print("Choose a door: 1, 2, or 3")

door = int(input("Enter your choice: "))

if door == 1:
    print("You found a treasure chest!")
elif door == 2:
    print("A friendly dragon gives you gold!")
elif door == 3:
    print("You escaped through a secret tunnel!")
else:
    print("Invalid door. Game Over!")