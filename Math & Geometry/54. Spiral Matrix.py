from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # turn and change directions when next is boundary
        # list of directions, 1.right 2.down 3.left 4.up
        res = []

        r,c = 0,-1
        right,bottom,left,top = len(matrix[0]),len(matrix),-1,-1 # boundary means don't go there. (exclusive)
        dir = "right"
        while len(res) != len(matrix) * len(matrix[0]):
            if dir == "right":
                while c+1 < right:
                    c += 1
                    res.append(matrix[r][c])
                top += 1
                dir = "down"
            elif dir == "down":
                while r+1 < bottom:
                    r += 1
                    res.append(matrix[r][c])
                right -= 1
                dir = "left"
            elif dir == "left":
                while c-1 > left:
                    c -= 1
                    res.append(matrix[r][c])
                bottom -= 1
                dir = "up"
            elif dir == "up":
                while r-1 > top:
                    r -= 1
                    res.append(matrix[r][c])
                left += 1
                dir = "right"
        return res

s= Solution()
m = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(s.spiralOrder(m))