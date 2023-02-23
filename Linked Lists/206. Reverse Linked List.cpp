/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head)//if no nodes
            return nullptr;
        if (!head->next)//if 1 node
            return head;
        if (!head->next->next) {//if 2 nodes
            head->next->next = head;
            head->next = nullptr;
            return head;
        }

        ListNode* prev = NULL;
        ListNode* cur = head;
        ListNode* n = cur->next;

        /*ListNode* prev = head;
        ListNode* cur = head->next;
        ListNode* n = cur->next;*/
        while (cur != nullptr) {//while n is not null
            cur->next = prev;
            prev = cur;
            cur = n;
            if (n != nullptr)//if n is not null
                n = n->next;
        }
        return prev;
    }
};