'''

============================= Leet Code Problem =============================

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)

        rank = {}

        for i in range(len(sorted_score)):
            if i == 0:
                rank[sorted_score[i]] = "Gold Medal"
            elif i == 1:
                rank[sorted_score[i]] = "Silver Medal"
            elif i == 2:
                rank[sorted_score[i]] = "Bronze Medal"
            else:
                rank[sorted_score[i]] = str(i + 1)

        res = []

        for s in score:
            res.append(rank[s])

        return res
        
===================================  Test  Cases  ===================================

'''

score = [10, 3, 8, 9, 4]

sorted_score = sorted(score, reverse=True)

rank = {}

for i in range(len(sorted_score)):
    if i == 0:
        rank[sorted_score[i]] = "Gold Medal"
    elif i == 1:
        rank[sorted_score[i]] = "Silver Medal"
    elif i == 2:
        rank[sorted_score[i]] = "Bronze Medal"
    else:
        rank[sorted_score[i]] = str(i + 1)

res = []

for s in score:
    res.append(rank[s])

print(res)