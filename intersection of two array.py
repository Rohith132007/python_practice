'''

=================================== Leet Code Problem ===================================

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        result = set1.intersection(set2)

        return list(result)
        
================================== Test Cases ========================================

'''

nums1 = list(map(int, input("Enter first array: ").split()))
nums2 = list(map(int, input("Enter second array: ").split()))

set1 = set(nums1)
set2 = set(nums2)

result = set1.intersection(set2)

print("Intersection:", list(result))
