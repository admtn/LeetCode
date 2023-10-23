from typing import List,Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        q.append(root)
        while q:
            levels_right = None
            for i in range(len(q)):
                popped = q.popleft()
                if popped:
                    levels_right = popped
                    q.append(popped.left)
                    q.append(popped.right)
            if levels_right:
                res.append(levels_right.val)

        return res  

a = TreeNode()
s = Solution()
print(s.rightSideView([1,2,3,None,5,None,4]))