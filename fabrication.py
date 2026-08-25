n = int(input())

a = 0
b = 1
i = 1

while True:
    print(a, end=" ")

    c = a + b
    a = b
    b = c
    i += 1

    if i > n:
        break