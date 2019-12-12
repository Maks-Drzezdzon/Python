# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, head1: ListNode, head2: ListNode) -> ListNode:
        ptr = ListNode(0)
        head = ptr
        
        if head1 == None:
            return head2
        if head2 == None:
            return head1
        
        while head1 != None and head2 != None:
            if head1.val <= head2.val:
                ptr.next = head1
                head1 = head1.next
            else:
                ptr.next = head2
                head2 = head2.next
            
            ptr = ptr.next
        
        if head1 != None:
            ptr.next = head1
        if head2 != None:
            ptr.next = head2
        
        return head.next
    