from typing import List
from collections import defaultdict
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        count = defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                count[board[i][j]] += 1
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        path = set()
        def dfs(i,r,c):
            if r not in range(len(board)) or c not in range(len(board[0])):
                return False
            if (r,c) in path:
                return False
            if board[r][c] != word[i]:
                return False
            if i == len(word)-1:
                return True
            
            path.add((r,c))
            if (
            dfs(i+1,r+1,c) or
            dfs(i+1,r-1,c) or
            dfs(i+1,r,c+1) or
            dfs(i+1,r,c-1)
            ):
                return True
            else:
                path.remove((r,c))
                return False

            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    if dfs(0,i,j):
                        return True
        return False

s = Solution()
print(s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],"ABCESEEEFS"))