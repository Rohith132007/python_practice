'''

=================================== Leet Code Problem ===================================

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n = n // 3

        return n == 1
        
==================================== Leet Code Problem ===================================

'''

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n = n // 3
            
        return n == 1
    
n = 27

solution = Solution()

answer = solution.isPowerOfThree(n)

print(answer)
