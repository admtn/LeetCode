class Solution {
public:
    int findMin(vector<int>& nums) {
        vector<int> result;
        int n = nums.size();
        if (n == 1)
            return nums[0];

        if (nums[0] < nums[n - 1])
            return nums[0];
        //left and right pointers
        int l = 0;
        int r = n - 1;
        int cur = (l + r) / 2;
        int min = INT_MAX;
        while (l <= r) {
            if (nums[cur] < min)
                min = nums[cur];

            if (nums[cur] >= nums[0]) {//too left, go right
                l = cur + 1;
            }
            else {//too right, go left
                r = cur - 1;
            }
            cur = (l + r) / 2;


        }

        return min;


    }

};
