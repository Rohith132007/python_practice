'''

=================================== Leet Code Problem =============================

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        res = majority = 0
        
        for n in nums:
            hash[n] = 1 + hash.get(n, 0)
            if hash[n] > majority:
                res = n
                majority = hash[n]
        
        return res
        
================================== Test Case ==============================

'''

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hash = {}
        res = majority = 0

        for n in nums:
            hash[n] = 1 + hash.get(n, 0)

            if hash[n] > majority:
                res = n
                majority = hash[n]

        return res


nums = [2, 2, 1, 1, 1, 2, 2]

solution = Solution()

answer = solution.majorityElement(nums)

print("Majority element:", answer)