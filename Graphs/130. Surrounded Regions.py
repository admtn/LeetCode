from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # change all the O that are connected to borders to N
        # change all the remaining Os to X
        # change back all the N to O

        border = set()
        rows, cols = len(board), len(board[0])

        def dfs(r,c):
            if (
                r not in range(rows) or
                c not in range(cols) or
                (r,c) in border or
                board[r][c] != "O"
                ): return
            
            board[r][c] = "N"
            border.add((r,c))
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
        for i in range(rows):
            if board[i][0] == "O": dfs(i,0)
            if board[i][cols-1] == "O": dfs(i,cols-1)

        for i in range(cols):
            if board[0][i] == "O":dfs(0,i)
            if board[rows-1][i] == "O":dfs(rows-1,i)
            
        # change remaining O to X
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "N":
                    board[i][j] = "O"     
    

s = Solution()
bo = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
s.solve(bo)
print(bo)