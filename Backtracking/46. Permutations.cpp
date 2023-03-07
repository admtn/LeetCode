#include <vector>
using namespace std;
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> sub;
        vector<vector<int>> result;
        dfs(nums,0,result,sub);
        return result;
    }

    void dfs(vector<int>&nums, int i,  vector<vector<int>>&result, vector<int>curr){
        //terminating condition is when size == 3
        if(curr.size() == nums.size()){
            result.push_back(curr);
            return;
        }
        //take 1st index
        curr.push_back(nums[i]);
        dfs(nums,i,result,curr);
        //take 2nd index
        curr.pop_back();
        dfs(nums,i+1,result,curr);
        //take 3rd index
        //.
        //.
        //.
        for(int j = 0; j < nums.size(); j++){
            if(nums[j])
            dfs(nums,j,result,curr);
        }
        
    }
};