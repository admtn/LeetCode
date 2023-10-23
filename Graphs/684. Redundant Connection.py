from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(1,len(edges)+1)}
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        cycle = {}
        # detect cycle
        def dfs(node,prev):
            if node in cycle:
                for key in list(cycle.keys()):
                    if key != node: del cycle[key]
                    else: return True
            cycle[node] = None
            
            for child in adj[node]:      
                if child == prev: continue
                if dfs(child,node): return True
            del cycle[node]
            return False
        
        dfs(edges[0][0],-1)
        for a,b in edges[::-1]:
            if a in cycle and b in cycle:
                return [a,b]
            

s = Solution()
ans = s.findRedundantConnection([[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]])
print(ans)
        