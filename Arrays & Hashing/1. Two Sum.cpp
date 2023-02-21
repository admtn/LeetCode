class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int, int> m;
        vector<int> answer;

        for (int i = 0; i < nums.size(); i++) {

            int complement = target - nums[i];
            if (m.find(complement) == m.end()) {//if doesnt exist
                m[nums[i]] = i;
            }
            else {
                answer.push_back(m[complement]);
                answer.push_back(i);
                break;
            }
        }

        return answer;
    }
};