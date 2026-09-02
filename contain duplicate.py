
'''
=========================== Leet Code Problem ===========================
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
            
        return False
        
============================ Leet Code Problem ===========================
        
'''
    
nums = [1, 2, 3, 4, 1]
nums.sort()

for i in range(1, len(nums)):
    if nums[i] == nums[i -1]:
        print(True)
        break
    
    else:
        print(False)
