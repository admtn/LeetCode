# Definition for singly-linked list.
from typing import List
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def getGradient(l,r):
            y_diff = r[1] - r[1]
            x_diff = r[0] - l[0]
            return y_diff/x_diff if x_diff else float('inf')
        
        m = getGradient(coordinates[0],coordinates[1])
        for i in range(len(coordinates)-1):
            temp = getGradient(coordinates[i],coordinates[i+1])
            if temp != m :
                return False
            m = temp
        
        return True
