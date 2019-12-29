# https://leetcode.com/problems/reverse-linked-list/submissions/ 99.11%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        current = head
        Next = None
        
        while current != None:
            Next = current.next
            current.next = previous
            previous = current
            current = Next 
        
        
        return previous