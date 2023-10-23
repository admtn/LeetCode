from typing import List
class Solution:
    # def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:


    #     rows = len(heights)
    #     cols = len(heights[0])

    #     res = []
    #     vis = set()

    #     def dfs(r,c): 
    #         if (r,c) in res: return (True,True)
    #         if c < 0 or r < 0: return(True,False)
    #         if r >= rows or c >= cols: return(False,True)
    #         if (r,c) in vis: return (False,False)
    #         vis.add((r,c))
    #         (pac,at) = (False,False)

    #         directions = [[-1,0],[1,0],[0,-1],[0,1]]

    #         # new spot is high, low, or sea.
    #         # allow if low or sea.
    #         for i,j in directions:
    #             nextR = r+i
    #             nextC = c+j
    #             if nextR not in range(rows) or nextC not in range(cols) or heights[nextR][nextC] <= heights[r][c] :
    #                 (curP,curA) = dfs(r+i,c+j)
    #                 (pac,at) = (curP or pac, curA or at)
    #         return (pac,at)
            


    #     for row in range(len(heights)):
    #         for col in range(len(heights[0])):
    #             (p,a) = dfs(row,col)
    #             if p and a:
    #                 res.append([row,col])
    #             vis.clear()
    #     return res

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atla = set(), set()
        res = []

        def dfs(r,c,vis:set,prevH):
            if (
                r not in range(rows) or
                c not in range(cols) or
                (r,c) in vis or
                prevH > heights[r][c]
                ): return
            
            vis.add((r,c))

            # down, up, right, left
            dfs(r+1,c,vis,heights[r][c])
            dfs(r-1,c,vis,heights[r][c])
            dfs(r,c+1,vis,heights[r][c])
            dfs(r,c-1,vis,heights[r][c])

        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atla,heights[r][cols-1])
        
        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atla,heights[rows-1][c])

        for i in range(rows):
            for j in range(cols):
                if (i,j) in pac and (i,j) in atla: res.append([i,j])

        return res

s = Solution()
ans  = s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
print(ans)