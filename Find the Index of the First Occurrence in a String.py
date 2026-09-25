'''

=================================== Leet Code Problem  ===================================

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1 

================================ Test Cases ===================================

'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack)):
            if haystack[i:i + len(needle)] == needle:
                return i

        return -1


haystack = input("Enter haystack: ")
needle = input("Enter needle: ")

obj = Solution()

result = obj.strStr(haystack, needle)

print("Output:", result)