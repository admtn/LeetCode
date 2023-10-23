from typing import List,Optional
from collections import defaultdict,deque
class Node:
    def __init__(self, key, val) -> None:
        self.key, self.val = key,val
        self.next, self.prev = None,None
class LRUCache:

    def __init__(self, capacity: int):
        self.left, self.right = Node(0,0), Node(0,0)
        self.map = {}
        self.c = capacity
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node:Optional[Node]):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self,node):
        mru = self.right.prev
        mru.next = node
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            # breaking the link
            node = self.map[key]
            self.remove(node)
            self.insert(node)
            node.val = value
        else:
            if len(self.map) >= self.c:
                self.map.pop(self.left.next.key)
                self.remove(self.left.next)
                newNode = Node(key,value)
                self.insert(newNode)
                self.map[key] = newNode
            else:
                # just starting out
                newNode = Node(key,value)
                self.map[key] = newNode
                self.insert(newNode)


            
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)