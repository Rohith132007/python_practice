'''

================================= Leet Code Problem ==============================

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)
        if len(nums) >= 3:
            return nums[2]
        else:
            return nums[0]
            
==================================== Test Cases ====================================

'''

class Solution:

    def thirdMax(self, nums: list[int]) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)

        if len(nums) >= 3:
            return nums[2]
        else:
            return nums[0]

nums = [3, 2, 1]

solution = Solution()

result = solution.thirdMax(nums)

print("Third maximum number:", result)