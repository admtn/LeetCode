class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        unordered_map<string,vector<string>> m;
        vector<vector<string>> result;

        for(int i = 0; i < strs.size(); i++){
            string key = getKey(strs[i]);
            m[key].push_back(strs[i]);
        }

        for(auto i = m.begin(); i != m.end(); i++){
            result.push_back(i->second);
        }

        return result;



        
    }

private:
    string getKey(string s){
        vector<int> count(26);
        for(int i = 0; i < s.size(); i++){
            count[s[i]-'a']++;
        }

        string key = "";
        for(int i = 0; i < count.size(); i++){
            key.append(to_string(count[i]+100));
        }

        return key;
    }
};