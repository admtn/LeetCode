class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {

        int m = matrix.size();
        int n = matrix[0].size();

        int toprow = 0;
        int botrow = m - 1;
        int midrow = m / 2;

        int row;

        while (toprow <= botrow) {
            if (matrix[midrow][0] == target)
                return true;
            else if (matrix[midrow][0] < target && target < matrix[midrow][n - 1]) {
                row = midrow;
                break;
            }
            else if (matrix[midrow][0] < target) {
                toprow = midrow + 1;
                midrow = (toprow + botrow) / 2;
            }
            else {
                botrow = midrow - 1;
                midrow = (toprow + botrow) / 2;
            }
        }

        int left = 0;
        int right = n - 1;
        int mid = n / 2;

        while (left <= right) {
            if (matrix[row][mid] < target) {
                left = mid + 1;
                mid = (left + right) / 2;
            }
            else if (matrix[row][mid] > target) {
                right = mid - 1;
                mid = (right + left) / 2;
            }
            else
                return true;
        }
        return false;

    }
};