#include <iostream>
using namespace std;


struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}

};

// //we can solve this problem by using extra space with sets, which
//is a less complicated solution, but we can use Floyd's tortoise and hare algorithm
//that takes no space at all and runes in O(n) time as well.
class Solution {
public:
    bool hasCycle(ListNode* head) {

        if (!head)
            return false;

        ListNode* slow = head;
        ListNode* fast = head;

        while (slow && fast) {
            slow = slow->next;
            for (int i = 0; i < 2; i++) {
                if (fast != NULL)
                    fast = fast->next;
                else
                    return false;
            }

            if (fast == slow)
                return true;
        }

        return false;
    }
};