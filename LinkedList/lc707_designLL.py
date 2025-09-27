"""
https://leetcode.com/problems/design-linked-list/description/
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0
        
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        current = self.head
        ix = 0
        while ix < index:
            ix += 1
            current = current.next
        return current.val
    
    def addAtHead(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            self.length += 1
            return
        next = self.head
        self.head = Node(val, next)
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            self.length += 1
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(val)
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
            return
        elif index == self.length:
            self.addAtTail(val)
            return
        current = self.head
        ix = 0
        while ix < index - 1:
            ix += 1
            current = current.next
        current.next = Node(val, current.next)
        self.length += 1
     
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        current = self.head
        ix = 0
        while ix < index - 1:
            ix += 1
            current = current.next
        current.next = current.next.next
        self.length -= 1
