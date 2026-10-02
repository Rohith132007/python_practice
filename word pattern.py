'''

================================== Leet Code Problem ================================

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        look = {}
        for p, w in zip(pattern, words):
            key_p = ("p", p)
            key_w = ("w", w)
            
            if key_p in look and look[key_p] != w:
                return False
            if key_w in look and look[key_w] != p:
                return False
            look[key_p] = w
            look[key_w] = p
        return True
        
================================ Test Cases ================================

'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        look = {}

        for p, w in zip(pattern, words):
            key_p = ("p", p)
            key_w = ("w", w)

            if key_p in look and look[key_p] != w:
                return False

            if key_w in look and look[key_w] != p:
                return False

            look[key_p] = w
            look[key_w] = p

        return True

pattern = input("Enter pattern: ")
s = input("Enter string: ")

solution = Solution()

result = solution.wordPattern(pattern, s)

print("Output:", result)