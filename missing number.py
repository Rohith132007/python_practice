'''

========================== Leet code Problem ==========================

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]

        return res
        
============================ Leet code Problem ==========================

'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        
        for i in range (len(nums)):
            res += i - nums[i]
            
        return res
    
nums = [3, 0, 1]
solution = Solution()
print(solution.missingNumber(nums))
