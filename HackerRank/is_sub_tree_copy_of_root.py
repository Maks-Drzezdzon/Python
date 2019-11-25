# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    string_s = self.traverse_tree(s)
    string_t = self.traverse_tree(t)
    if string_t in string_s:
        return True
    return False


def traverse_tree(self, s):
    if s:
        return f"#{s.val} {self.traverse_tree(s.left)} {self.traverse_tree(s.right)}"
    return None     
