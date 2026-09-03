'''

============================== Leet Code Problem ==============================

class Solution:
    def reverseBits(self, n: int) -> int:
        
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1

        return result

============================= Leet code Problem ==============================

'''

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for i in range(32):
            result =(result << 1) | (n & 1)
            n >>= 1
        return result

n = int(input("Enter the Number: "))
solution = Solution()
result = solution.reverseBits(n)
print("the reverse the bits of the number is:", result)