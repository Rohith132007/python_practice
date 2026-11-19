'''

================================= Leet Code Problem =================================

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numbers = set(nums)
        res = []

        for n in range(1, len(nums) + 1):
            if n not in numbers:
                res.append(n)
        
        return res
        
================================== Test  Cases ==================================

'''


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        numbers = set(nums)
        res = []

        # Check numbers from 1 to length of array
        for n in range(1, len(nums) + 1):
            if n not in numbers:
                res.append(n)

        return res


# Main program
nums = [4, 3, 2, 7, 8, 2, 3, 1]

obj = Solution()
result = obj.findDisappearedNumbers(nums)

print("Input:", nums)
print("Disappeared numbers:", result)
