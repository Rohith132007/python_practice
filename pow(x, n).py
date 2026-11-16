'''

============================== Leet Code Problem ==================================

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return pow(x, n)
        
==============================  Test Cases  ===========================

'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # If power is negative, take reciprocal of x
        if n < 0:
            x = 1 / x
            n = -n
        #initialized the value for res 
        res = 1.0
        # Repeat until power becomes 0
        while n > 0:
            if n % 2 != 0:
                res = res * x

            x = x * x
            n = n // 2

        return res


obj = Solution()

x = float(input("Enter x: "))
n = int(input("Enter n: "))

result = obj.myPow(x, n)

print("Output:", result)
