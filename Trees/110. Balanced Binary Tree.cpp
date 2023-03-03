/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        //check if left is balanced
        //check if right is balanced
        //check if itself is balanced
        if (!root)
            return true;

        bool balanced = isBalanced(root->left) && isBalanced(root->right);
        if (!balanced)
            return false;
        //if balanced, check if itself is balanced

        int left = getMaxHeight(root->left);
        int right = getMaxHeight(root->right);
        if (abs(left - right) > 1)
            return false;
        else
            return true;



    }

    int getMaxHeight(TreeNode* root) {
        if (!root)
            return 0;

        return max(getMaxHeight(root->left), getMaxHeight(root->right)) + 1;
    }
};