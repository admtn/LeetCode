class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int maxprofit = INT_MIN;
        int l = 0;
        int r = 0;
        while (r <= n - 1) {

            if (prices[l] > prices[r]) {
                l = r;
                r++;
                continue;
                if (r >= n)
                    break;
            }
            int profit = prices[r] - prices[l];
            if (profit > maxprofit)
                maxprofit = profit;
            r++;
        }

        return maxprofit;
    }
};