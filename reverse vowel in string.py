'''

===================================== Leet Code Problem ==============================

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"

        v = []

        for ch in s:
            if ch in vowels:
                v.append(ch)

        v.reverse()

        result = ""

        for ch in s:
            if ch in vowels:
                result += v.pop(0)
            else:
                result += ch

        return result
        
=============================== Test Cases ===============================

'''


s = input("Enter a string: ")

vowels = "aeiouAEIOU"
v = []

# Collect vowels
for ch in s:
    if ch in vowels:
        v.append(ch)

# Reverse the vowels
v.reverse()

result = ""

# Replace vowels in the original string
for ch in s:
    if ch in vowels:
        result += v.pop(0)
    else:
        result += ch

print("Reversed vowels:", result)

