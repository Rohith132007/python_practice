'''

================================= Leet Code Problem ================================

class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        mapping = {")":"(", "}":"{","]":"["}
        
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or stack.pop() != mapping[char]:
                    return False
        return not stack
        
================================== Leet Code Problem ================================

'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping.values():
                stack.append(char)

            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False

        return not stack

solution = Solution()

s = input("Enter brackets: ")

result = solution.isValid(s)

print("Output:", result)