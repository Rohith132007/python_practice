'''

================================= Leet Code Problem ================================

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"
        result = ""

        num = num & 0xFFFFFFFF

        while num > 0:
            remainder = num % 16
            result = hex_chars[remainder] + result
            num = num // 16

        return result

================================  Test Cases =================================

'''


num = 26

hex_chars = "0123456789abcdef"
result = ""

if num == 0:
    result = "0"
else:
    num = num & 0xFFFFFFFF

    while num > 0:
        remainder = num % 16
        result = hex_chars[remainder] + result
        num = num // 16

print(result)
