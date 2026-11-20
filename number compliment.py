'''

==============================  Leet Code Problem =============================

class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]

        complement = ""

        for bit in binary:
            if bit == "0":
                complement += "1"
            else:
                complement += "0"

        return int(complement, 2)

================================  Test  Csaes  ==============================

'''


class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]

        complement = ""

        for bit in binary:
            if bit == "0":
                complement += "1"
            else:
                complement += "0"

        return int(complement, 2)


# Main program
num = 5

obj = Solution()
print(obj.findComplement(num))
