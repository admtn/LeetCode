# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # same if left(a) == left(b)
        # and right(a) == right(b)
        # and the node itself is same
        def Same(a: Optional[TreeNode], b: Optional[TreeNode]):
            if a == None and b == None:
                return True
            if a == None or b == None:
                return False
            
            return a.val == b.val and Same(a.left,b.left) and Same(a.right,b.right)
        return Same(p,q)
