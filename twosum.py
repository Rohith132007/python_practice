def twoSum(nums, target):
    seen = {}

    for i in range(len(nums)):
        difference = target - nums[i]

        if difference in seen:
            return [seen[difference], i]

        seen[nums[i]] = i

# Test
nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))