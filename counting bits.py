'''

================================== Leet Code Problem ==================================

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        sub = 1

        for i in range(1, n + 1):
            if sub * 2 == i:
                sub = i
            
            dp[i] = dp[i - sub] + 1
        
        return dp
        
=================================== Test Cases ==================================

'''

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        sub = 1

        for i in range(1, n + 1):
            if sub * 2 == i:
                sub = i

            dp[i] = dp[i - sub] + 1

        return dp

n = int(input("Enter n: "))

solution = Solution()

result = solution.countBits(n)

print("Number of 1s:", result)