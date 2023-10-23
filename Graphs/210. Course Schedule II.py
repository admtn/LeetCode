from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hash = { i:[] for i in range(numCourses)}
        for c,p in prerequisites:
            hash[c].append(p)
        
        visit = set()
        order = []


        # dfs checks if a course can be completed
        def dfs(crs):
            if crs in visit: return False
            if hash[crs] == []:
                if crs not in order:
                    order.append(crs)
                return True
            visit.add(crs)
            for preC in hash[crs]:
                if not dfs(preC): return False
            visit.remove(crs)
            hash[crs] = []
            if crs not in order:
                order.append(crs)
            return True

        for crse in range(numCourses):
            if not dfs(crse): return []
        
        return list(order)
    
s = Solution()
ans = s.findOrder(2,[[0,1]])
print(ans)