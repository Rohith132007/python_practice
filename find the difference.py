'''

=================================== Leet Code Problem ===================================

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for ch in t:
            if t.count(ch) > s.count(ch):
                return ch
                
=================================== Test Cases ===================================

'''
s = input("Enter string s: ")
t = input("Enter string t: ")

for ch in t:
    if t.count(ch) > s.count(ch):
        print("Extra character:", ch)
        break