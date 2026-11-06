'''

================================ Leet Code Problem ==================================

class Solution:
    def countSegments(self, s: str) -> int:
        words = s.split()
        return len(words)
        
================================  Test  Cases  ==================================

'''
s = "Hello, my name is John"

count = 0

words = s.split()

count = len(words)

print(count)