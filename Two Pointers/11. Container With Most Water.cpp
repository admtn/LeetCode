class Solution {
public:

    int smaller(int a, int b) {
        if (a <= b)
            return a;
        else
            return b;
    }

    int maxArea(vector<int>& height) {
        int max = INT_MIN;
        int left = 0;
        int right = height.size() - 1;
        while (left < right) {
            int area = smaller(height[left], height[right]) * (right - left);
            if (area > max)
                max = area;

            if (height[left] <= height[right])
                left++;
            else
                right--;
        }
        return max;
    }




};