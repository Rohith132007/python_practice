'''

====================================== Leet Code Problem ===================================

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {}
        first = {}
        last = {}

        for i, n in enumerate(nums):

            if n not in count:
                count[n] = 0
                first[n] = i

            count[n] += 1
            last[n] = i

        degree = max(count.values())

        res = len(nums)

        for n in count:
            if count[n] == degree:
                length = last[n] - first[n] + 1
                res = min(res, length)

        return res

==================================== Test Cases =====================================

'''


nums = [1, 2, 2, 3, 1]

count = {}
first = {}
last = {}

# Count frequency and store first and last positions
for i, n in enumerate(nums):

    if n not in count:
        count[n] = 0
        first[n] = i

    count[n] += 1
    last[n] = i

# Find maximum frequency
degree = max(count.values())

res = len(nums)

# Find shortest subarray
for n in count:

    if count[n] == degree:
        length = last[n] - first[n] + 1
        res = min(res, length)

print(res)
