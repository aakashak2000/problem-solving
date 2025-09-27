"""
https://leetcode.com/problems/add-two-numbers/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1, current2 = l1, l2
        head = ListNode()
        current = head
        carry = 0
        while current1 and current2:
            val = current1.val + current2.val + carry
            if val >= 10:
                carry = 1
                val -= 10
            else:
                carry = 0
            Node = ListNode(val)
            current.next = Node
            current = current.next
            current1 = current1.next
            current2 = current2.next

        while current1:
            val = current1.val + carry
            if val >= 10:
                carry = 1
                val -= 10
            else:
                carry = 0
            Node = ListNode(val)
            current.next = Node
            current = current.next
            current1 = current1.next
        
        while current2:
            val = current2.val + carry
            if val >= 10:
                carry = 1
                val -= 10
            else:
                carry = 0
            Node = ListNode(val)
            current.next = Node
            current = current.next
            current2 = current2.next

        if carry > 0:
            current.next = ListNode(carry)
        return head.next