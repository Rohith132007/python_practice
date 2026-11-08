'''

=================================== Leet Code Problem ===================================

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        else:
            return max(len(a), len(b))

====================================  Test Cases  ======================================

'''

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        else:
            return max(len(a), len(b))


# Input
a = "aba"
b = "cdc"

obj = Solution()
print(obj.findLUSlength(a, b))