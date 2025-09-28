"""
https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/
"""
class Solution:
    def findWinners(self, matches):
        lost = {}
        for w, l in matches:
            lost[l] = lost.get(l, 0) + 1
            lost[w] = lost.get(w, 0)
        lost0 = sorted([l for l in lost if lost[l] == 0])
        lost1 = sorted([l for l in lost if lost[l] == 1])

        return [lost0, lost1]
            
