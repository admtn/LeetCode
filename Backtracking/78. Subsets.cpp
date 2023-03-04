#include <vector>
using namespace std;
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> sub;

        dfs(0,nums,result,sub);
        return result;
    }

    void dfs(int i, vector<int>&nums, vector<vector<int>>&result,vector<int>&sub){
        if(i >= nums.size() ){
            result.push_back(sub);
            return;
        }
        //include
        sub.push_back(nums[i]);
        dfs(i+1,nums,result,sub);

        //dont include
        sub.pop_back();
        dfs(i+1,nums,result,sub);
    }
};