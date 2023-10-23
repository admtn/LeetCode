from typing import List, Optional
from collections import deque
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class mySolution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def traverse(ar:deque,node:Optional[ListNode]):
            while node:
                ar.append(node.val)
                node = node.next
        
        def getInt(num:List):
            temp = ""
            for i in range(len(num)-1,-1,-1):
                temp += str(num[i])
            return int(temp)
        
        num_1 = []
        num_2 = []
        traverse(num_1,l1)
        traverse(num_2,l2)
        
        int_1 = getInt(num_1)
        int_2 = getInt(num_2)

        res_string = str(int_1 + int_2)
        node = ListNode(int(res_string[0]),None)
        for i in range(1,len(res_string)):
            newNode = ListNode(int(res_string[i]),node)
            node = newNode
        
        return node

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        dummy = ListNode()
        cur = dummy 
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            value = v1 + v2

            if carry:
                value += 1
                carry = 0

            if value >= 10:
                carry = 1
                value -= 10

            cur.next = ListNode(value)
            cur = cur.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next           

        return dummy.next