from typing import List
class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        # check all directions (u,d,l,r,diagonalL,diagonalR)
        # the first cell needs to be opposite color
        # then the last cell needs to be same color

        # up : rMove -= 1
        # down : rMove += 1
        # left : c -= 1
        # right : c += 1
        # topleft : r -= 1, c -= 1
        # topright : r -= 1, c += 1
        # botleft : r += 1, c -= 1
        # botright : r += 1, c += 1
        opp = "W" if color == "B" else "B"
        dir = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
        def check(direction):
            rd,cd = direction
            r,c = rMove+rd , cMove+cd
            length = 1
            while r in range(8) and c in range(8) and board[r][c] == opp:
                r += rd
                c += cd
                length += 1
            if r in range(8) and c in range(8) and board[r][c] == color and length >= 2:
                return True
            else:
                return False
        for d in dir:
            if check(d):
                return True
        return False


s = Solution()
ans = [["W","W",".","B",".","B","B","."],["W","B",".",".","W","B",".","."],["B","B","B","B","W","W","B","."],["W","B",".",".","B","B","B","."],["W","W","B",".","W",".","B","B"],["B",".","B","W",".","B",".","."],[".","B","B","W","B","B",".","."],["B","B","W",".",".","B",".","."]]
print(s.checkMove(ans,7,4,"B"))