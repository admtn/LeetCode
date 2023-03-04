class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        //diameter of current node is left height + right height + 2
        //height of current node is max(left subtree height, right subtree height) + 1
        int result = 0;
        maxHeight(root, result);
        return result;
    }

    int maxHeight(TreeNode* root, int& diameter) {
        if (!root)
            return -1;
        int leftHeight = maxHeight(root->left,diameter);
        int rightHeight = maxHeight(root->right,diameter);
        diameter = max(leftHeight + rightHeight + 2,diameter);
        return 1 + max(leftHeight, rightHeight);
    }
};