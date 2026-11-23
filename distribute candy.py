'''

============================= Leet Code Problem ==============================

class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        
        unique_candies = set(candyType)

        return min(len(unique_candies), len(candyType) // 2)

============================== Test Cases =================================

'''

# Distribute Candies

candyType = [1, 1, 2, 2, 3, 3]

# Remove duplicate candy types
unique_candies = set(candyType)

# Find the maximum number of different candies
result = min(len(unique_candies), len(candyType) // 2)

# Print the answer
print(result)
