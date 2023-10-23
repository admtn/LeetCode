from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}
        def dfs(r,c,pre):
            if (
                r not in range(len(matrix)) or
                c not in range(len(matrix[0])) or
                matrix[r][c] <= pre) : return 0
            
            if (r,c) in cache:
                return cache[(r,c)]
            
            res = 1 + max(
                dfs(r+1,c,matrix[r][c]), # down
                dfs(r-1,c,matrix[r][c]), # up
                dfs(r,c+1,matrix[r][c]), # right
                dfs(r,c-1,matrix[r][c])  # left
            )
            cache[(r,c)] = res
            return res
        
        ans = float('-inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans,dfs(i,j,float('-inf')))
        return ans

class SolutionWithComments:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # find the LIP for each starting point
        # get the longest
        # dfs returns the longest increasing path starting from index (r,c)
        cache = {}
        def dfs(r,c,pre):
            if (
                # time complexity to check INT in range on range objects is O(1) in python 3.x
                # for float it is O(n)
                # IN operator on lists object is O(n) be it INT or FLOAT
                # so we can use not in range over 0 <= r < len(matrix) because it is the same 
                r not in range(len(matrix)) or
                # not (0 <= r < len(matrix)) or
                c not in range(len(matrix[0])) or
                matrix[r][c] <= pre
            ): return 0
            # return cache first, or else it doesn't work. because it skips base case which return 0
            if (r,c) in cache:
                return cache[(r,c)]

            # run dfs on adjacent higher cells, and append 1 at the end.
            res = 1 + max(
                dfs(r+1,c,matrix[r][c]), # down
                dfs(r-1,c,matrix[r][c]), # up
                dfs(r,c+1,matrix[r][c]), # right
                dfs(r,c-1,matrix[r][c])  # left
            )
            cache[(r,c)] = res
            return res

        ans = float('-inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans,dfs(i,j,float('-inf')))
        return ans
        # return dfs(2,1,0)

s = Solution()
print(s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))