#include <utility>
using namespace std;

struct TreeNode {
    int val ;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int maxDepth(TreeNode* root) {
        //max depth of tree is max( left depth, right depth) + 1
        if (!root)
            return 0;
        return 1 + max(maxDepth(root->left), maxDepth(root->right));

    }
};