n = int(input())

i = 1

while True:
    j = 1

    while True:
        print(j, end="")
        j += 1

        if j > i:
            break

    print()
    i += 1

    if i > n:
        break
    