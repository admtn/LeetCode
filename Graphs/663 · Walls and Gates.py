from typing import (
    List,
)
from collections import deque
class Solution:
    def walls_and_gates(self, rooms: List[List[int]]):
        q = deque()
        vis = set()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    vis.add((i,j))
                    q.append((i,j))
        
        def addroom(i,j):
            if (i,j) in vis or i not in range(len(rooms)) or j not in range(len(rooms[0])) or rooms[i][j] == -1:
                return
            else:
                q.append((i,j))
                vis.add((i,j))

        dist = 0
        while q:
            for x in range(len(q)):
                i,j = q.popleft()
                rooms[i][j] = dist
                addroom(i-1,j) # up
                addroom(i+1,j) # down
                addroom(i,j-1) # left
                addroom(i,j+1) # right
            dist += 1 # dist represents the distance from the nearest gate to all the current nodes in the queue.
        
        return rooms


            

"""
class Solution:
    def walls_and_gates(self, rooms: List[List[int]]):

        def bfs(i,j):
            vis = set()
            q = deque()
            q.append((i,j,0))
            while q:
                x,y,d = q.popleft()
                rooms[x][y] = min(rooms[x][y],d)
                dir = [[1,0],[-1,0],[0,1],[0,-1]] # down, up, right, left
                for up,down in dir:
                    newX = x+up
                    newY = y+down
                    if newX in range(len(rooms)) and newY in range(len(rooms[0])) and rooms[newX][newY] not in [-1,0] and (newX,newY) not in vis:
                        q.append((newX,newY,1+d))
                        vis.add((newX,newY))
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    bfs(i,j)
        return rooms





class Solution:

    def walls_and_gates(self, rooms: List[List[int]]):
        vis = set()
        cache = {}
        # dfs returns distance to the nearest gate for that coordinate
        def dfs(i,j):
            if (i,j) in vis:
                return float('inf')
            if (
                i not in range(len(rooms)) or
                j not in range(len(rooms[0])) or
                rooms[i][j] == -1
                ):
                return float('inf')
            if rooms[i][j] == 0:
                return 0
            if (i,j) in cache:
                return cache[(i,j)]

            vis.add((i,j))
            res = min(
                dfs(i+1,j),
                dfs(i-1,j),
                dfs(i,j+1),
                dfs(i,j-1)
            ) + 1
            vis.remove((i,j))
            cache[(i,j)] = res
            return res
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 2147483647:
                    vis.clear()
                    rooms[i][j] = dfs(i,j)
        return rooms
"""
s = Solution()
print(s.walls_and_gates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))