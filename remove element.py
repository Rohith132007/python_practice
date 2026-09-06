'''

================================ Leet Code Problem ================================
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
        
================================= Leet Code Problem ================================

'''

class Solution:
    def removeElement(self, nums, val):
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


# Input
nums = [3, 2, 2, 3]
val = 3

# Create object
solution = Solution()

# Call the function
k = solution.removeElement(nums, val)

# Output
print("Number of elements:", k)
print("Array after removing", val, ":", nums[:k])
        