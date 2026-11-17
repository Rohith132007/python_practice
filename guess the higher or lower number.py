'''

============================== Leet Code Problem ===========================

class Solution:
    def guessNumber(self, n: int) -> int:

        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2

            result = guess(mid)

            if result == 0:
                return mid

            elif result == -1:
                right = mid - 1

            else:
                left = mid + 1

==============================  Test Cases  ==============================

'''

# Secret number
secret = 6

# Guess function
def guess(num):
    if num > secret:
        return -1
    elif num < secret:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:

        # Starting range
        left = 1
        right = n

        # Repeat until number is found
        while left <= right:

            # Find middle number
            mid = (left + right) // 2

            # Check the guessed number
            result = guess(mid)

            if result == 0:
                return mid

            elif result == -1:
                right = mid - 1

            else:
                left = mid + 1


# Create object
obj = Solution()

# Call function
n = 10
answer = obj.guessNumber(n)

print("Secret number found:", answer)
