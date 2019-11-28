
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def util(self, node):
            if node not in self.dic:
                new = Node(node.val, None, None)
                self.dic.update({node:new})
            return self.dic[node]

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        node = head
        self.dic = {}
        while node:
            if node not in self.dic:
                self.dic.update({node:Node(node.val, None, None)})
            new = self.dic[node]
            if node.next:
                new.next = self.util(node.next)
            elif not node.next:
                new.next = None
            if node.random:
                new.random = self.util(node.random)
            elif not node.random:
                new.random = None
            node = node.next
        return self.dic[head]
