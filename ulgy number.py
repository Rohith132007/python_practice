'''

================================= Leet Code roblem =================================

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n % 2 == 0:
            n = n // 2
        while n % 3 == 0:
            n = n // 3
        while n % 5 == 0:
            n = n // 5

        return n == 1
        
================================ Test Cases ==================================

'''
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2== 0 or n % 3 ==0 or n % 5 == 0:
            if n % 2 == 0:
                n = n // 2
            elif n % 3 == 0:
                n = n // 3
            elif n % 5 == 0:
                n = n // 5
                
            return n == 1
        
obj = Solution()

n = 30

print(obj.isUgly(n))