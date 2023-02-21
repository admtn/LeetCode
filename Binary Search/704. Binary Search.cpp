class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        int l = 0;
        int r = n - 1;
        int i = n / 2;


        if (nums[0] > target || nums[n - 1] < target)
            return -1;

        while (l <= r) {
            if (nums[i] < target) {
                l = i + 1;
                i = (l + r) / 2;
            }
            else if (nums[i] > target) {
                r = i - 1;
                i = (l + r) / 2;
            }
            else
                return i;
        }

        return -1;

    }
};