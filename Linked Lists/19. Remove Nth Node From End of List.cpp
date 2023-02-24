class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {

        ListNode* fast = head, * slow = head;
        if (!head || !head->next) //if 0 or 1 node, return null because n>=1 so need to remove it.
            return NULL;

        for (int i = 0; i < n + 1; i++) {
            if (fast != NULL) {
                fast = fast->next;
            }
            else {//if fast node goes out of bounds, means need to remove the head node aka the first node
                head = head->next;
                return head;
            }
        }

        while (fast != NULL) {
            slow = slow->next;
            fast = fast->next;
        }

        slow->next = slow->next->next;
        return head;
    }
};