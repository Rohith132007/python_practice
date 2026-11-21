'''

===================================== leet code problem ==============================

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = 0
        for i in range(len(nums)):
            if i > goal:
                return False

            goal = max(goal, i + nums[i])
        return True

================================  Test Cases ==============================

'''
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = 0
        for i in range(len(nums)):
            if i > goal:
                return False

            goal = max(goal, i + nums[i])
        return True

nums = [2, 3, 1, 1, 4]

obj = Solution()
print(obj.canJump(nums))