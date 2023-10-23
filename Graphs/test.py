from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:        

        adj_list, cycle = {}, {}
        for a,b in edges:
            adj_list.setdefault(a,[]).append(b)
            adj_list.setdefault(b,[]).append(a)
        
        # dfs checks whether the node and its parent is part of a cycle and return true if it is.
        # it also creates a dict of all the nodes involved in the cycle.
        def dfs(node, parent):
            if node in cycle:
                for k in list(cycle.keys()):
                    if k == node:
                        return True
                    del cycle[k]   
            cycle[node] = None
            for child in adj_list[node]:
                if child != parent and dfs(child,node):
                    return True
            del cycle[node]
            return False
            
        dfs(edges[0][0],-1)
        for a,b in edges[::-1]:
            if a in cycle and b in cycle:
                return (a,b)
            
s = Solution()
ans = s.findRedundantConnection([[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]])
print(ans)