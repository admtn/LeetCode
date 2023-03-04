
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:

    int goodNodes(TreeNode* root) {
        //inorder traversal , itself, left, right
        int max = root->val;
        return good(root,max);
    }
    int good(TreeNode*root, int max){
        if(!root)
            return 0;
        if(root->val >= max){
            max = root->val;
            return good(root->left,max)+good(root->right,max)+1;
        }
        else{
            return good(root->left,max)+good(root->right,max);
        }
    }
};