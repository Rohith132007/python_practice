'''

==================================== Leet code Problem ================================

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        total = 0

        for i in range(1, num):
            if num % i == 0:
                total += i

        return total == num
        
================================ Test Cases ================================

'''


num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Perfect Number")
else:
    total = 0

    for i in range(1, num):
        if num % i == 0:
            total = total + i

    if total == num:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")
