'''

=================================== Leet code Problrm ===================================

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = ""

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                digit1 = int(num1[i])
            else:
                digit1 = 0

            if j >= 0:
                digit2 = int(num2[j])
            else:
                digit2 = 0

            total = digit1 + digit2 + carry

            result = str(total % 10) + result
            carry = total // 10

            i -= 1
            j -= 1

        return result
        
======================================== Test case ================================

'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = ""

        while i >= 0 or j >= 0 or carry:
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0

            total = digit1 + digit2 + carry

            result = str(total % 10) + result
            carry = total // 10

            i -= 1
            j -= 1

        return result


num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

obj = Solution()

answer = obj.addStrings(num1, num2)

print("Sum =", answer)