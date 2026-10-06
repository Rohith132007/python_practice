'''

=================================== Leet Code Problem ===================================

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)

        i = 0
        while i < len(s):
            s[i:i + k] = reversed(s[i:i + k])
            i = i + 2 * k  

        return "".join(s)   

==================================== Test Cases ====================================

'''

def reverseStr(s, k):
    s = list(s)

    i = 0

    while i < len(s):
        s[i:i + k] = reversed(s[i:i + k])
        i = i + 2 * k

    return "".join(s)


s = "abcdefg"
k = 2

result = reverseStr(s, k)

print("Original string:", s)
print("k =", k)
print("Reversed string:", result)