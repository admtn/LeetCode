from typing import List
from collections import defaultdict
class DetectSquares:

    def __init__(self):
        self.points = []
        

    def add(self, point: List[int]) -> None:
        self.points.append(point)

    def numPoints(self,point: List[int]):
        res = 0
        for x,y in self.points:
            if x == point[0] and y == point[1]:
                res += 1
        return res
    
    def count(self, point: List[int]) -> int:
        # how to detect diagonal?
        # get equation of the line.
        qX, qY = point[0],point[1]
        # y = x + c  -> y - x = c , positive m
        c1 = qY - qX
        # y = -x + c -> y + x = c , negative m
        c2 = qY + qX
        res = 0
        for x,y in self.points:
            if x == qX and y == qY: # square cannot be infinitely small
                continue
            if y-x == c1: # positive m
                a,b = self.numPoints([x,qY]),self.numPoints([qX,y])
                print(f"postiive m, a: {a}  b: {b}   a*b: {a*b}")
                res += a*b
            if y+x == c2: # negative m
                a,b = self.numPoints([x,qY]),self.numPoints([qX,y])
                print(f"negative m, a: {a}  b: {b}   a*b: {a*b}")
                res += a*b
        print(f"Count for [{qX,qY}]: {res}")
        print()
        return res


class DetectSquares:
    def __init__(self):
        self.points = []
        self.map = defaultdict(int)
        
    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.map[(point[0],point[1])] += 1
    
    def count(self, point: List[int]) -> int:
        qX, qY = point[0],point[1]
        res = 0
        for x,y in self.points:
            if x == qX and y == qY: # square cannot be infinitely small
                continue
            if y-x == qY - qX: # positive m
                res += self.map[(x,qY)] * self.map[(qX,y)]
            if y+x == qY + qX: # negative m
                res += self.map[(x,qY)] * self.map[(qX,y)]
        return res
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)