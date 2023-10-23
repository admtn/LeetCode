from typing import List,Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        heads = [] # list of heads we need to reverse
        r_heads = [] # list of heads of the reversed heads
        def reverse(node: Optional[ListNode], k):
            pre,cur,nex = None,node,node.next
            cnt = 0
            while cnt < k:
                cur.next = pre
                pre = cur
                cur = nex
                if nex:
                    nex = nex.next
                cnt += 1
            # new tail, new head
            return (node,pre)
        
        i = 0
        cur = head 
        while cur: # to create a lists of heads we need to reverse, also to count total number of nodes so we can check for leftovers
            if i%k == 0:
                heads.append(cur)
            i += 1
            cur = cur.next
        
        # to reverse all the heads in the list
        if i%k:  # if there are leftovers
            for i in range(len(heads)):
                if i == len(heads)-1:
                    r_heads.append((None,heads[i]))
                else:
                    r_heads.append(reverse(heads[i],k))
        else:   # if no leftovers
            for i in range(len(heads)):
                r_heads.append(reverse(heads[i],k))
        
        # to connect the newly reversed lists
        for i in range(len(heads)-1):
            # tail of left connect to head of right 
            r_heads[i][0].next = r_heads[i+1][1]

        return r_heads[0][1]

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        


s = Solution()
n = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,ListNode(7)))))))
ans = s.reverseKGroup(n,4)
while ans:
    print(ans.val)
    ans = ans.next