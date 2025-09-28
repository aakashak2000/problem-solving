"""
https://leetcode.com/problems/reverse-linked-list/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        if head is None or head.next is None:
            return head

        prevNode = ListNode()
        current = head
        nextNode = current.next

        while current:
            current.next = prevNode
            prevNode = current
            current = nextNode
            if current:
                nextNode = current.next
        head.next = None
        return prevNode

