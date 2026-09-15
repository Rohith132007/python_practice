'''

================================ Leet Code Problem ================================
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        prev1 = 3
        prev2 = 2
        cur = 0

        for _ in range(3, n):
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur

        return cur
        
================================ Leet Code Problem ================================

'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        prev1 = 3
        prev2 = 2
        cur = 0

        for _ in range(3, n):
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur

        return cur
        
n = 5

solution = Solution()

answer = solution.climbStairs(n)
print("input:", n)
print("output:", answer)       
        
