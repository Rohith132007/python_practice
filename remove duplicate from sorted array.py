'''

================================ Leet Code problem ================================

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                nums[i] = nums[j]
                i += 1

        return i
        
================================ Leet code Problem ================================

'''

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                nums[i] = nums[j]
                i += 1

        return i


solution = Solution()

nums = [1, 1, 2]

k = solution.removeDuplicates(nums)

print("k =", k)
print("nums =", nums[:k])

