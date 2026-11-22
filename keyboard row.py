'''

=========================== Leet Code Problem ============================

class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"

        result = []

        for word in words:
            word_lower = word.lower()

            if all(char in row1 for char in word_lower):
                result.append(word)

            elif all(char in row2 for char in word_lower):
                result.append(word)

            elif all(char in row3 for char in word_lower):
                result.append(word)

        return result
        
=================================  Test Cases  =================================

'''



# Keyboard Row - LeetCode 500

class Solution:
    def findWords(self, words):

        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"

        result = []

        for word in words:
            word_lower = word.lower()

            if all(char in row1 for char in word_lower):
                result.append(word)

            elif all(char in row2 for char in word_lower):
                result.append(word)

            elif all(char in row3 for char in word_lower):
                result.append(word)

        return result


# Main program
words = ["Hello", "Alaska", "Dad", "Peace", "letter"]

obj = Solution()

answer = obj.findWords(words)

print("Input:", words)
print("Output:", answer)


