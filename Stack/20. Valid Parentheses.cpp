class Solution {
public:
    bool isValid(string s) {
        stack<int> st;
        for (auto i = s.begin(); i != s.end(); i++) {
            char c = *i;
            switch (c) {
            case '(':st.push(c); break;
            case ')':
                if (st.empty() || st.top() != '(')
                    return false;
                st.pop();
                break;
            case '{':st.push(c); break;
            case '}':
                if (st.empty() || st.top() != '{')
                    return false;
                st.pop();
                break;
            case '[':st.push(c); break;
            case ']':
                if (st.empty() || st.top() != '[')
                    return false;
                st.pop();
                break;
            }
        }
        if (!st.empty())
            return false;
        return true;
    }
};