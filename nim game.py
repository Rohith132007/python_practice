'''

=============================== Leet Code Problem ================================

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
        
================================= Test Cases ===================================

'''

n = int(input("Enter number of stones: "))

if n % 4 != 0:
    print(True)
else:
    print(False)