'''

================================== Leet Code Problem ==================================

class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)

            total = 0

            while n > 0:
                digit = n % 10
                total += digit * digit
                n = n // 10

            n = total

        return True
        
================================ Test Cases ==================================

'''

def isHappy(n):

    seen = set()

    while n != 1:
        if n in seen:
            return False

        seen.add(n)

        total = 0

        while n > 0:
            digit = n % 10
            total += digit * digit
            n = n // 10

        n = total

    return True


# Get input from user
n = int(input("Enter a number: "))

# Check happy number
if isHappy(n):
    print("Happy Number")
else:
    print("Not a Happy Number")
