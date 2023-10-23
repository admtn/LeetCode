from typing import List,Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # for each node, calculate its split (itself + left no split + right no split )and update res
        # then calculate its no split to return to the parent ( itself + max(left,right,0) )
        res = float('-inf')
        
        # dfs returns itself.val + max(left single, right single)
        # and calculates its own split max (to update res)
        def dfs(node:Optional[TreeNode]):
            nonlocal res
            if not node:
                return 0
            
            leftSingle = dfs(node.left)
            rightSingle = dfs(node.right)
            res = max( res, node.val + leftSingle + rightSingle)
            return max( node.val + max(leftSingle,rightSingle), 0 )
        
        dfs(root)

        return res

