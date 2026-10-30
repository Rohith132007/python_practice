'''

========================================= leet code Problem ===============================

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        i = 0
        j = 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result
        
====================================  Test Cases =================================

'''

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()

        i = 0
        j = 0
        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1

            elif nums1[i] < nums2[j]:
                i += 1

            else:
                j += 1

        return result

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

obj = Solution()

answer = obj.intersect(nums1, nums2)

print("Intersection:", answer)