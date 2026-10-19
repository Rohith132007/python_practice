'''

================================== Leet Code Problem ==================================

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                a = ord(num1[i]) - ord('0')
                b = ord(num2[j]) - ord('0')

                total = a * b + result[i + j + 1]

                result[i + j + 1] = total % 10
                result[i + j] += total // 10

        answer = ""
        started = False

        for digit in result:
            if digit != 0:
                started = True

            if started:
                answer += chr(digit + ord('0'))

        return answer

===================================== Test Cases =====================================

'''


def multiply(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"

    result = [0] * (len(num1) + len(num2))

    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num2) - 1, -1, -1):
            a = ord(num1[i]) - ord('0')
            b = ord(num2[j]) - ord('0')

            total = a * b + result[i + j + 1]

            result[i + j + 1] = total % 10
            result[i + j] += total // 10

    answer = ""
    started = False

    for digit in result:
        if digit != 0:
            started = True

        if started:
            answer += chr(digit + ord('0'))

    return answer


num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print("Product:", multiply(num1, num2))
