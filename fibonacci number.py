'''

================================ Leet Code Problem ==================================

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        a = 0
        b = 1

        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c

        return b

====================================  Test Cases =====================================

'''


n = int(input("Enter n: "))

if n == 0:
    print(0)

elif n == 1:
    print(1)

else:
    a = 0
    b = 1

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    print("Fibonacci number:", b)
