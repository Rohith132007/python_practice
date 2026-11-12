'''

=================================== Leet code problem ======================================

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}

        for i, val in enumerate(nums):
            if val in seen and i - seen[val] <= k:
                return True
            else:
                seen[val] = i

        return False 
        
====================================  Test Cases ========================================

'''

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen:
                if abs(i - seen[nums[i]]) <= k:
                    return True

            seen[nums[i]] = i

        return False

nums = [1, 0, 1, 1]
k = 1

obj = Solution()
result = obj.containsNearbyDuplicate(nums, k)

print("Output:", result)
