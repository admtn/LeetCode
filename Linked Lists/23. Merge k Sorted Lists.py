from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class mySolution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def getSmallest(nodes: List[Optional[ListNode]]):
            dummyNode = ListNode(float('inf'),)
            index = None
            for i in range(len(lists)):
                if lists[i] and lists[i].val < dummyNode.val:
                    dummyNode = lists[i]
                    index = i
            if index == None:
                return False
            return (dummyNode,index)
        
        dummy = ListNode()
        cur = dummy
        while lists:
            t = getSmallest(lists)
            if not t:
                break
            # update res list and cur pointer
            cur.next = t[0]
            cur = cur.next

            # update the heads in the lists
            i = t[1]
            lists[i] = lists[i].next
            if not lists[i]: lists.pop(i)

            # lists[t[1]] = lists[t[1]].next if lists[t[1]].next else lists.pop(t[1])
        return dummy.next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None


        temp_lists = []
        while len(lists) > 1:
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                temp_lists.append(self.merge(l1,l2))
            lists = temp_lists
            temp_lists = []
        
        return lists[0]

    def merge(self,a:Optional[ListNode],b:Optional[ListNode]):
        dummy = ListNode()
        cur, curA, curB = dummy, a,b
        while curA and curB:
            if curA.val < curB.val:
                cur.next = curA
                curA = curA.next # shift a pointer
            else:
                cur.next = curB
                curB = curB.next
            cur = cur.next
        
        if curA:
            cur.next = curA
        if curB:
            cur.next = curB

        return dummy.next






s = Solution()
k1 = ListNode(1,ListNode(4,ListNode(5)))
k2 = ListNode(1,ListNode(3,ListNode(4)))
k3 = ListNode(2,ListNode(6))
head = s.mergeKLists([k1,k2,k3])
cur = head
while cur:
    print(cur.val)
    cur = cur.next

