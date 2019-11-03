# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/ 99.34%

class Solution(object):
    def removeNthFromEnd(self, head, n):
        # variables
        place = head
        length = 0
        
        #iter over nodelist
        while place:
            place = place.next
            length += 1
        # count len of vars
        # if len is 5, 4-2 = 2 delete 3rd element in node list
        place = head
        step = length - n 
        # if its 0 delte next
        if step == 0:
            head = head.next
        else:
            # otherwise iter over list till you get to step of 
            l = 1
            while l < step:
                place = place.next
                l += 1
            place.next = place.next.next
            
        return head
        
        