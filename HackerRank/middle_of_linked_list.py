# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        
        if head == None:
            return head
            
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        
        return slow