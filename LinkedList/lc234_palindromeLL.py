"""
https://leetcode.com/problems/palindrome-linked-list/description/
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        
        def reverseLL(head):
            if not head or not head.next:
                return head
            prev = ListNode()
            current = head
            nextNode = head
            while current:
                nextNode = current.next
                current.next = prev
                prev = current 
                current = nextNode
            head.next = None
            return prev

        def findMiddle(head):
            if not head or not head.next:
                return head
            fast, slow = head, head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        middle = findMiddle(head)
        rev = reverseLL(middle)

        l1, l2 = head, rev
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return True
