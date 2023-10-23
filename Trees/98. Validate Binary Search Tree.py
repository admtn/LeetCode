from typing import List,Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # this function checks if a node is valid
        # it is valid if left child smaller than itself
        # right child bigger than itself
        # it is within the boundaries of its parents
        def validNode(node:Optional[TreeNode],left,right):
            if not node:
                return True
            if not left < node.val < right:
                return False
            return(
                validNode(node.left,left,node.val) and
                validNode(node.right,node.val,right)
            )
        return validNode(root,float('-inf'),float('inf'))
