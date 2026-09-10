'''

============================= Leet Code Problem =============================

class Solution:
    def lengthOfLastWord(self, s: str) -> int:                
        length = 0
        counting = False

        for c in s:
            if c != " ":
                if not counting:
                    counting = True
                    length = 1
                else:
                    length += 1
            else:
                counting = False
        
        return length
        
=============================== Leet Code Problem =============================

'''

def lengthOfLastWord(s):
    length = 0
    counting = False

    for c in s:
        if c != " ":
            if not counting:
                counting = True
                length = 1
            else:
                length += 1
        else:
            counting = False

    return length

s = input("Enter a string: ")

result = lengthOfLastWord(s)

print("Length of last word:", result)