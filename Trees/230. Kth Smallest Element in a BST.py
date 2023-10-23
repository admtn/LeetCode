from typing import List,Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        def inorder(r: Optional[TreeNode]):
            # left, itself, right
            if not r:
                return
            if len(nodes) == k:
                return
            inorder(r.left)
            if len(nodes) == k:
                return
            nodes.append(r.val)
            if len(nodes) == k:
                return
            inorder(r.right)
            if len(nodes) == k:
                return
        
        inorder(root)
        return nodes[k-1]


    
class Stack:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur,q = root,deque()
        while cur and q:
            while cur:
                q.append(cur)
                cur = cur.left
            
            cur = q.pop()
            k -= 1
            if k == 0:
                return cur.val
            q.append(cur.right) 
            cur = cur.right
        