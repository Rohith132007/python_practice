'''

================================== Leet Code Problem ======================================

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        result = []

        for num in arr:
            result.append(num)

            if num == 0:
                result.append(0)

        arr[:] = result[:len(arr)]

====================================== Test Cases ==========================================

'''


arr = list(map(int, input("Enter array elements: ").split()))

result = []

for num in arr:
    result.append(num)

    if num == 0:
        result.append(0)

arr[:] = result[:len(arr)]

print("Output:", arr)
