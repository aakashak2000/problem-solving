"""
https://leetcode.com/problems/middle-of-the-linked-list/description/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head):
        if head.next is None:
            return head

        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow