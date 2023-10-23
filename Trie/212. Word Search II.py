from typing import List

class TrieNode:
    def __init__(self, children = {}, end = False, char = None) -> None:
        self.children = {}
        self.end = end
        self.char = char
    
    def addWord(self, word:str):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode(char = c)
            cur = cur.children[c]
        cur.end = True

class Solution:
    def __init__(self) -> None:
        self.count = 0

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.count = len(words)
        ROW,COL = len(board),len(board[0])
        root = TrieNode()
        for w in words:
            root.addWord(w)
        res = []
        def dfs(r,c,node:TrieNode,cur_word):
            if (
                (r,c) in vis or
                r not in range(ROW) or 
                c not in range(COL) or
                self.count == 0 or
                board[r][c] not in node.children
                ):
                return
            vis.add((r,c))
            node = node.children[board[r][c]]
            cur_word += board[r][c]
            if node.end:
                res.append(cur_word)
                node.end = False
                self.count -= 1
            dfs(r+1,c,node,cur_word)
            dfs(r-1,c,node,cur_word)
            dfs(r,c+1,node,cur_word)
            dfs(r,c-1,node,cur_word)
            vis.remove((r,c))
            
        vis = set()
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] in root.children:
                    dfs(i,j,root,"")
                vis.clear()
        return res
