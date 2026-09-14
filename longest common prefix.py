'''

================================== Leetcode Problem: Longest Common Prefix ==================================

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        pref_len = len(pref)

        for s in strs[1:]:
            while pref != s[0:pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ""
                
                pref = pref[0:pref_len]
        
        return pref
        
==================================== Leet Code Problem ====================================

'''

class Solution:
    def longestCommonPrefix(self, strs):
        pref = strs[0]
        pref_len = len(pref)

        for s in strs[1:]:
            while pref != s[0:pref_len]:
                pref_len -= 1

                if pref_len == 0:
                    return ""

                pref = pref[0:pref_len]

        return pref


strs = ["flower", "flow", "flight"]

solution = Solution()

result = solution.longestCommonPrefix(strs)

print("Strings:", strs)
print("Longest Common Prefix:", result)