class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        //range from 1 to biggest int in the vector;
        int small = 1;
        int big = *max_element(piles.begin(), piles.end());
        int mid = (1 + big) / 2;
        int k = INT_MAX;

        while (small <= big) {
            if (getTotal(piles, mid) > h) {//eat too slow, increase the rate k
                small = mid + 1;
                mid = (small + big) / 2;
            }
            else if (getTotal(piles, mid) <= h) { // eat too fast, decrease rate k because we want min k.check if smaller k.
                k = mid;
                big = mid - 1;
                mid = (small + big) / 2;
            }
        }


        return k;


    }

    long int getTotal(vector<int>& vec, int eat) {
        long int hours = 0;
        for (int i = 0; i < vec.size(); i++) {
            hours += ceil((double)vec[i] / eat);
        }
        return hours;
    }


};