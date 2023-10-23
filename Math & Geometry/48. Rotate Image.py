from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)
        # Formula, NEW ROW = OLD COL, NEW COL = N-1 - OLD ROW
        for i in range(n//2):
            length = n - i*2 # length of side of square
            for j in range(i,i+length-1): # swap length-1 times 
                r,c = i,j 
                matrix[r][c], matrix[c][n-r-1], matrix[n-r-1][n-c-1], matrix[n-c-1][n-(n-r-1)-1] = \
                matrix[n-c-1][n-(n-r-1)-1], matrix[r][c], matrix[c][n-r-1], matrix[n-r-1][n-c-1]
class Transpose:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for row in matrix:
            row.reverse()

class Boundaries:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        



                    

s = Solution()
g = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s.rotate(g)
print(g)