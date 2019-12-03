# Definition for singly-linked list.
# https://leetcode.com/problems/merge-two-sorted-lists/submissions/
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None


def mergeTwoLists(self, head1: ListNode, head2: ListNode):
    head = ptr = ListNode(0)
    
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    
    # go through both lists and compare nodes
    while(head1 and head2):
        if (head1.val < head2.val):
            ptr.next = head1
            head1 = head1.next
            
        elif (head1.val >= head2.val):
            ptr.next = head2
            head2 = head2.next
            
        ptr = ptr.next
    
    # if one list is longer than the other finish the rest of the list with the longer list since they are already sorted 
    ptr.next = head1 or head2
    return head.next

'''
# java version 
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode head1, ListNode head2) {
        ListNode ptr = new ListNode(0);
        ListNode head = ptr;
        
        if(head1==null) {
            return head2;
        }
        
        if(head2==null) {
            return head1;
        }
        
        while(head1 != null && head2 != null){
            if(head1.val <= head2.val) {
                ptr.next = head1;
                head1 = head1.next;
            } else {
                ptr.next = head2;
                head2 = head2.next;
            }
            ptr = ptr.next;
        }
        
        if(head1!=null) {
            ptr.next = head1;
        }
        
        if(head2!=null) {
            ptr.next = head2;
        }
        
        
        return head.next;
        
    }
}


'''