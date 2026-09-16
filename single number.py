''' 

================================ Leet Code Problem ================================

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0

        for n in nums:
            res ^= n

        return res
        
================================ Leet Code Problem ================================

'''

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0

        for n in nums:
            res ^= n

        return res


nums = [4, 1, 2, 1, 2]

solution = Solution()

answer = solution.singleNumber(nums)

print("Single number:", answer)