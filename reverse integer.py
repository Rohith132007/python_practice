'''

================================== Leet Code Problem ==================================

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            digit = x % 10
            x = x // 10
            result = result * 10 + digit
        result = result * sign

        if result < (-2**31) or result > (2**31) - 1:
            return 0
        
        return result

=================================== Test Cases =====================================

'''

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1 
        
        result = int(str(abs(x))[::-1])*sign
        if result < (-2**31) or result > (2**31) - 1:
            return 0
        return result
    
x = int(input("Enter an integer: "))
solution = Solution()
print("Reversed integer:", solution.reverse(x))