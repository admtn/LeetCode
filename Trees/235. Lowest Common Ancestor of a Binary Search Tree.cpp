
 struct TreeNode {
     int val;
     TreeNode *left;
   TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };
 

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(p == root || q == root)//if equal, then itself is ancestor
            return root;
        if( (p->val > root->val && q->val < root->val) || (p->val<root->val && q->val > root->val) )//if split
            return root;
        
        if(p->val > root->val && q->val > root->val)
            return lowestCommonAncestor(root->right,p,q);
        else
            return lowestCommonAncestor(root->left,p,q);
    }
}; 