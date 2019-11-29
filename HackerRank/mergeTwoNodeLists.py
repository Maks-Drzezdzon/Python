# Definition for singly-linked list.
# https://leetcode.com/problems/merge-two-sorted-lists/submissions/
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, head1, head2):
        head = ptr = ListNode(0)
        
        # go through both lists and compare nodes
        while(head1 and head2):
            if (head1.val < head2.val):
                ptr.next = head1
                head1 = head1.next
                # stores prev value
                ptr = ptr.next
                
            elif (head1.val >= head2.val):
                ptr.next = head2
                head2 = head2.next
                # stores prev value
                ptr = ptr.next
        
        # if one list is longer than the other finish the rest of the list with the longer list since they are already sorted 
        ptr.next = head1 or head2
        return head.next
        