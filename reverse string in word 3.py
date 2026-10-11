'''

================================= leet code Problem ====================================

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        result = []

        for word in words:
            reverse_word = word[::-1]
            result.append(reverse_word)


        return " ".join(result)
        
================================   Test Cases   =====================================

'''

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        result = []

        for word in words:
            reverse_word = word[::-1]
            result.append(reverse_word)

        return " ".join(result)

solution = Solution()

s = input("Enter a sentence: ")
answer = solution.reverseWords(s)
print("Reversed words:", answer)