from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for j in range(n)]
        col = set()
        ldiag = set()
        rdiag = set()
        def dfs(r):
            if r == n:
                copy = []
                for i in board:
                    copy.append(''.join(i))
                res.append(copy.copy())
                return
            
            for c in range(n):
                if (
                    c not in col and
                    (r+c) not in ldiag and
                    (r-c) not in rdiag
                ):
                    board[r][c] = 'Q'
                    col.add(c)
                    ldiag.add(r+c)
                    rdiag.add(r-c)
                    dfs(r+1)
                    board[r][c] = '.'
                    col.remove(c)
                    ldiag.remove(r+c)
                    rdiag.remove(r-c)
        dfs(0)
        return res

s = Solution()
print(s.solveNQueens(4))