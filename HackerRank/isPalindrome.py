 class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr, cur = [], head
        while cur:  
            arr.append(cur.val)
            cur = cur.next 
        return arr == arr[::-1]