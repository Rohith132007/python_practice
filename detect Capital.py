'''

================================== Leet Code Problem ==================================

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True
        if word.islower():
            return True
        if word[0].isupper() and word[1:].islower():
            return True
        
        return False
        
================================ Test Cases =========================================

'''

word = input("Enter a word: ")

if word.isupper():
    result = True

elif word.islower():
    result = True

elif word[0].isupper() and word[1:].islower():
    result = True

else:
    result = False

print(result)