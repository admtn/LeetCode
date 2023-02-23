class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char, int> m;
        int length = s1.size();
        int counter = length;
        for (int i = 0; i < s1.size(); i++) {
            m[s1[i]]++;
        }

        //left and right pointers
        int l = 0;
        int r = 0;
        while (r <= s2.size() - 1) {
            if (m.find(s2[r]) == m.end() || m[s2[r]] == 0) {//if key not found or key empty
                //reset counter
                if (l == r) {//if no elements was deducted from map
                    r++;
                    l++;
                    counter = length;
                }
                else {//if elements were deducted from map
                    counter++;
                    m[s2[l]]++;//add them back
                    l++;

                }
            }
            else {//if found key in map
                m[s2[r]]--;
                counter--;
                if (counter == 0)
                    return true;
                r++;
            }
        }
        return false;

    }
};