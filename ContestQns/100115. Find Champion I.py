from typing import List
class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        N = len(grid)
        for i in range(N):
            cnt = 0
            for j in range(N):
                if grid[i][j] == 1:
                    cnt += 1
                    if cnt == N-1:
                        return i
print(Solution().findChampion([[0,0,1],[1,0,1],[0,0,0]]))