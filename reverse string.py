'''
 
=================================== Leetcode Problem ==================================

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        
=================================== Test case ==================================

'''

class Solution:

    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

s = ["h", "e", "l", "l", "o"]

obj = Solution()

obj.reverseString(s)

print(s)

