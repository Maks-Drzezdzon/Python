class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        Next = None
        current = head
        previous = None
        
        while current != None:
            Next = current.next
            current.next = previous
            previous = current
            current = Next
             
            
            
        return previous