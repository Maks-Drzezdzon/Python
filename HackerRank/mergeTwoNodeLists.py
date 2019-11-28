# Definition for singly-linked list.
# https://leetcode.com/problems/merge-two-sorted-lists/submissions/
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, head1, head2):
        head = sort_list = ListNode(0)
        
        while(head1 and head2):
            if (head1.val < head2.val):
                sort_list.next = head1
                head1 = head1.next
                sort_list = sort_list.next
                
            elif (head1.val >= head2.val):
                sort_list.next = head2
                head2 = head2.next
                sort_list = sort_list.next

        sort_list.next = head1 or head2
        return head.next
        