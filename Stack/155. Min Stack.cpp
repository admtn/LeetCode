class MinStack {
public:
    MinStack() {

    }

    void push(int val) {

        //min before pushing currently is minStk.top().second

        if (stk.empty()) {

            pair<int, int> newpair(val, val);
            minStk.push(newpair);
            stk.push(val);
        }
        else {

            if (val < minStk.top().second) {
                pair<int, int> newpair(val, val);
                minStk.push(newpair);
            }
            else {
                pair<int, int>newpair(val, minStk.top().second);
                minStk.push(newpair);
            }
            stk.push(val);
        }


    }

    void pop() {
        stk.pop();
        minStk.pop();
    }

    int top() {
        return stk.top();
    }

    int getMin() {
        return minStk.top().second;
    }

private:
    stack<int> stk;
    stack<pair<int, int>> minStk;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */