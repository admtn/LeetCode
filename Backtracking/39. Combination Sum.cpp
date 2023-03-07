#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> results;
        vector<int>sub;
        subsets(candidates,results,sub,target,0, 0);
        return results;

    }

    void subsets(vector<int>&candidates, vector<vector<int>>&results, vector<int>&sub, int target, int i, int sum){
        //results need to have & as we want the value of results to be saved when we
        //alter it, such as results.push_back(sub). if no &, then when return is called, the results
        //vector will be in its original state.
        //sub doesn't need & because we don't need to retain/save its changes because at the end of the
        //recursive function call we push_back it into results. but if we put & it still works because we still pop it.
        //basically pass by value vs pass by reference.

        //base cases
        if(i >= candidates.size())
            return;
        if( sum == target ){
            results.push_back(sub);
            return;
        }

        if( sum > target )
            return;

        //include
        sub.push_back(candidates[i]);
        subsets(candidates,results,sub,target,i,sum+candidates[i]);
        sub.pop_back();
        //dont include, go next
        subsets(candidates,results,sub,target,i+1,sum);
        return;
    }
};