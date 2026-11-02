'''

================================ Leet Code Problem ================================

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i

        return -1
        
================================== Test Cases ===================================

'''

s = input("Enter a string: ")

for i in range(len(s)):
    if s.count(s[i]) == 1:
        print("First unique character:", s[i])
        print("Index:", i)
        break
else:
    print("No unique character found")