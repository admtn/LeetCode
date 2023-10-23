from typing import List
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # checking rows
        for r in range(len(board)):
            vis = set()
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                if board[r][c] in vis:
                    return False
                vis.add(board[r][c])
            vis.clear()

        # checking cols
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[c][r] == '.':
                    continue
                if board[c][r] in vis:
                    return False
                vis.add(board[c][r])
            vis.clear()

        def invalidSquare(i,j):
            SqSet = set()
            for a in range(3):
                for b in range(3):
                    if board[i+a][j+b] == '.':
                        continue
                    if board[i+a][j+b] in SqSet:
                        return True
                    SqSet.add(board[i+a][j+b])

        for i in range(0,7,3):
            for j in range(0,7,3):
                if invalidSquare(i,j):
                    return False
        
        return True

class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqs = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in sqs[(r//3,c//3)]:
                    return False
                
                if board[r][c] != '.':
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    sqs[(r//3,c//3)].add(board[r][c])
        return True


s = Solution2()

        