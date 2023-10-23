from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create list of nodes, store their adresses
        # do the next and val
        # return to list then store their random vals using list
        if not head: return None
        nodes = []
        cur = head
        # creating the nodes
        index = 0
        while cur:
            obj = Node(cur.val)
            cur.val = index
            nodes.append([obj,cur.random]) # [obj, og's random's address]
            cur = cur.next
            index += 1

        # doing next and random
        for i in range(len(nodes)):
            if i != len(nodes)-1:
                nodes[i][0].next = nodes[i+1][0]
            ind = nodes[i][1].val if nodes[i][1] else None
            nodes[i][0].random = nodes[ind][0] if ind != None else None

        return nodes[0][0]
        
        
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        oldtocopy = {None:None}
        cur = head
        while cur:
            copy = Node(cur.val)
            oldtocopy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            oldtocopy[cur].next = oldtocopy[cur.next]
            oldtocopy[cur].random = oldtocopy[cur.random]
            cur = cur.next
        
        return oldtocopy[head]
