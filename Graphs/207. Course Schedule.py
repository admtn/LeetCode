from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        hash = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            hash[crs].append(pre)
        visit = set()
        
        # dfs checks if a course can be finished
        def dfs(c):
            if hash[c] == []: return True
            if c in visit : return False
            visit.add(c)
            for prq in hash[c]:
                if not dfs(prq): return False
            visit.remove(c)
            hash[c] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course): return False
        
        return True




# s = Solution()
# ans = s.canFinish(2,[[1,0]])
# print(ans)


            
