class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {

        vector<vector<int>> result;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            if (i != 0 && nums[i] == nums[i - 1])
                continue;
            int target = 0 - nums[i];
            int left = i + 1;
            int right = nums.size() - 1;
            while (left < right) {
                int sum = nums[left] + nums[right];
                if (sum < target) {
                    left++;
                }
                else if (sum > target) {
                    right--;
                }
                else {
                    vector<int> r = { nums[i],nums[left],nums[right] };
                    result.push_back(r);
                    left++;
                    right--;
                    while (nums[left] == nums[left - 1] && left < right)
                        left++;
                    while (nums[right] == nums[right + 1] && left < right)
                        right--;
                }
            }
        }

        return result;
    }
};