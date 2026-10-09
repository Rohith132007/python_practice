'''

=================================== Leet Code Solution =================================

    def reverseOnlyLetters(self, s: str) -> str:
        letters = list(filter(str.isalpha, s))
        letters.reverse()

        result = ""
        for ch in s:
            if ch.isalpha():
                result += letters.pop(0)
            else:
                result += ch

        return result
        
==================================== test Cases ===========================================

'''
s = input("Enter a string: ")

letters = list(filter(str.isalpha, s))
letters.reverse()

result = ""

for ch in s:
    if ch.isalpha():
        result += letters.pop(0)
    else:
        result += ch

print("Reversed string:", result)