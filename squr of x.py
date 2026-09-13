'''

================================== Leet Code Problem ==========================

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        i = 2
        while i * i <= x:
            i += 1

        return i - 1
        
================================ Leet Code Problem ==========================

'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        i = 2

        while i * i <= x:
            i += 1

        return i - 1


x = int(input("Enter a number: "))
obj = Solution()

result = obj.mySqrt(x)

print("Integer square root:", result)