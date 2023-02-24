class Solution {
public:
    void reorderList(ListNode* head) {

        if (head->next == NULL || head->next->next == NULL)//if 1 or 2 nodes
            return;


        ListNode* slow = head;
        ListNode* fast = head->next;
        while (fast->next != NULL) {//break if fast is pointing to tail
            for (int i = 0; i < 2; i++) {
                if (fast->next != NULL)//ensures that fast pointer will point to the tail and not be null
                    fast = fast->next;
            }
            slow = slow->next;
        }
        ListNode* tail1 = slow;
        slow = slow->next;
        ListNode* pre = NULL;
        ListNode* cur = slow;
        ListNode* n = slow->next;
        while (cur) {
            cur->next = pre;
            pre = cur;
            cur = n;
            if (n) //if n is not null
                n = n->next;
        }
        tail1->next = NULL;
        //after reversing the list, pre will be the new head
        cur = head;
        ListNode* n1 = head->next;
        ListNode* n2 = pre->next;
        while (pre) {
            cur->next = pre;
            pre->next = n1;

            cur = n1;
            if (n1)
                n1 = n1->next;
            pre = n2;
            if (n2)
                n2 = n2->next;
        }
    }
};