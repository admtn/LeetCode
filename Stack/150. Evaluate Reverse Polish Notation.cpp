class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;

        for (int i = 0; i < tokens.size(); i++) {

            string t = tokens[i];


            if (t.size() > 1 || isdigit(t[0]))
                s.push(stoi(t));
            else {
                int a = s.top();
                s.pop();
                int b = s.top();
                s.pop();
                int c = 0;
                string dog = tokens[i];
                if (dog == "+") {
                    c = b + a;
                }
                else if (dog == "-") {
                    c = b - a;
                }
                else if (dog == "/") {
                    c = b / a;
                }
                else {
                    c = b * a;
                }
                s.push(c);
            }
        }

        return s.top();
    }
};