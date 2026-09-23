'''

================================ Leet Code Problem ================================

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 4 == 0:
            n = n // 4

        return n == 1
        
================================= Test Cases =================================

'''


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 4 == 0:
            n = n // 4

        return n == 1
    
n = 16
solution = Solution()
result = solution.isPowerOfFour(n)
print(result)