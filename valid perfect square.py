'''

================================== Leet Code Problem ================================

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1, num + 1):
            if i * i == num:
                return True

            if i * i > num:
                return False

        return False

================================ Test Cases ================================

'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1, num+1):
            if i *i == num:
                return True
            if i *i > num:
                return False
        return False
    
num = int(input("Enter the Number: "))
solution = Solution()
print(solution.isPerfectSquare(num))