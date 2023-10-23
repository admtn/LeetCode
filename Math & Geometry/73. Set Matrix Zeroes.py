from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = set()
        c = set()
        # O(mn)
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)
        # O(m)
        for n in r:
            for col in range(cols): #O*
                matrix[n][col] = 0
        # O(n)
        for n in c:
            for row in range(rows):
                matrix[row][n] = 0

class Solution:
    # no space used
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows, cols = len(matrix), len(matrix[0])
        def setNone(r,c):
            for i in range(rows):
                if matrix[i][c] == 0:
                    matrix[i][c] = None
                    setNone(i,c)
                matrix[i][c] = None
            for i in range(cols):
                if matrix[r][i] == 0:
                    matrix[r][i] = None
                    setNone(r,i)
                matrix[r][i] = None
                    

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    setNone(i,j)
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == None:
                    matrix[i][j] = 0