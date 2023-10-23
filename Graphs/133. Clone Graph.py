
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        mymap = {}
        def clone(oldnode:'Node'):
            if oldnode in mymap:
                return mymap[oldnode]
            
            new = Node(oldnode.val)
            mymap[oldnode] = new
            for i in oldnode.neighbors:
                new.neighbors.append(clone(i))
            
            return new
        
        return clone(node) if node else None
