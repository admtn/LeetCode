class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {

        int n = temperatures.size();
        stack<pair<int, int> > st; //int and index
        vector<int> result(n);

        for (int i = 0; i < n; i++) {
            pair<int, int> p(temperatures[i], i);
            if (i == 0) {
                st.push(p);
                continue;
            }
            while (!st.empty() && temperatures[i] > st.top().first) {
                result[st.top().second] = i - st.top().second;
                st.pop();
            }
            st.push(p);
        }

        while (!st.empty()) {
            result[st.top().second] = 0;
            st.pop();
        }
        return result;

    }
};