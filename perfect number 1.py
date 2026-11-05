'''

==================================== Leet code Problem ================================

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        if num <= 1:
            return False

        total = 1

        for i in range(2, int(num ** 0.5) + 1):

            if num % i == 0:
                total += i

                if i != num // i:
                    total += num // i

        return total == num
        
================================  test cases ================================

'''


num = int(input("Enter a number: "))

if num <= 1:
    print(False)
else:
    total = 1

    for i in range(2, int(num ** 0.5) + 1):

        if num % i == 0:
            total += i

            if i != num // i:
                total += num // i

    if total == num:
        print(True)
    else:
        print(False)
