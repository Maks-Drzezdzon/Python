# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/ 99.34%

class Solution(object):
    def removeNthFromEnd(self, head, n):
        p = head
        i = 0
        while p:
            p = p.next
            i += 1
        p = head
        step = i-n #total length - n
        if step == 0:
            head = head.next
        else:
            l = 1
            while l<step :
                p = p.next
                l += 1
            p.next = p.next.next
        return head
        