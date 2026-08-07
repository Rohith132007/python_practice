day = int(input("Enter a number (1-3): "))

switch = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday"
}

print(switch.get(day, "Invalid input"))