print("=== Fortune Teller ===")

color = input("Choose a color (red, blue, green, yellow): ").lower()

if color == "red":
    print("You will have a lucky day!")
elif color == "blue":
    print("A surprise is waiting for you.")
elif color == "green":
    print("Success is coming your way.")
elif color == "yellow":
    print("Today is a great day to learn something new.")
else:
    print("The future is a mystery. Try one of the given colors.")