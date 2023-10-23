# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
from collections import deque
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def Same(a:Optional[TreeNode], b:Optional[TreeNode]):
            if a == None and b == None:
                return True
            if a == None or b == None:
                return False
            
            return a.val == b.val and Same(a.left,b.left) and Same(a.right,b.right)

        q = deque()
        q.append(root)
        while q:
            temp = q.popleft()
            if temp:
                q.append(temp.left)
                q.append(temp.right)
                if temp.val == subRoot.val and Same(temp,subRoot):
                    return True
        return False
        


            