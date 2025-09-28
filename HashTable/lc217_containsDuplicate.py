"""
https://leetcode.com/problems/contains-duplicate/description/
"""
class Solution:
    def containsDuplicate(self, nums):
        count = {}
        for num in nums:
            if num in count:
                return True
            count[num] = 1
        return False
