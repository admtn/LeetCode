from typing import List
from collections import deque
class dfsCache:
    # this solution doesn't work because
    # dfs is not optimal. However, I take the min of each path, so it is optimal.
    # but I face TLE problem, so I added caching.
    # but caching with dfs doesn't make it optimal anymore, because when I use dfs
    # on the nodes, it caches the result on the node, even though that result might not be optimal.
    # as opposed to just letting run dfs on the node again to find the optimal/min path.
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def isDiff1(w1,w2):
            counter = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    counter += 1
            return True if counter <= 1 else False
        if beginWord not in wordList:
            wordList.append(beginWord)
        # O(n)
        adjList = { word:[] for word in wordList }
        # O(n^2*m)
        for w1 in adjList:
            for w2 in wordList:
                if w1 == w2:
                    continue
                if isDiff1(w1,w2):
                    adjList[w1].append(w2)
        
        # dfs returns the minimum num of steps to reach endWord from w
        # if it cannot reach endWord, it returns 0
        
        vis = set()
        cache = {}

        # this doesn't work as explained above
        def dfs(w):
            if w == endWord:
                return 1
            if w in vis:
                return 0
            if w in cache:
                return cache[w]
            
            canReach = False
            minSteps = float('inf')
            vis.add(w)
            for neighbor in adjList[w]:
                temp = dfs(neighbor)
                if temp:
                    canReach = True
                    minSteps = min(minSteps,temp)
            vis.remove(w)
            cache[w] = minSteps+1 if canReach else 0
            return cache[w]
        
        # this would work after revision from faang interviewer at reddit.
        # the key was to make the visited set part of the key in the cache.
        def dfs(w):
            if w == endWord:
                return 1
            if w in vis:
                return 0
            if (w,tuple(vis)) in cache:
                return cache[(w,tuple(vis))]
            
            canReach = False
            minSteps = float('inf')
            vis.add(w)
            for neighbor in adjList[w]:
                temp = dfs(neighbor)
                if temp:
                    canReach = True
                    minSteps = min(minSteps,temp)
            vis.remove(w)
            cache[(w,tuple(vis))] = minSteps+1 if canReach else 0
            return cache[(w,tuple(vis))]
        
        return dfs(beginWord)

class bfs:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def isDiff1(w1,w2):
            counter = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    counter += 1
            return True if counter <= 1 else False
        if beginWord not in wordList:
            wordList.append(beginWord)
        # O(n)
        adjList = { word:[] for word in wordList }
        # O(n^2*len(w))
        for w1 in adjList:
            for w2 in wordList:
                if w1 == w2:
                    continue
                if isDiff1(w1,w2):
                    adjList[w1].append(w2)
        q = deque()

        res = 0
        size = 1
        vis = set()
        q.append(beginWord)
        while q:
            for i in range(len(q)):
                temp = q.popleft()
                if temp == endWord:
                    return res+1
                for frens in adjList[temp]:
                    if frens not in vis:
                        q.append(frens)
                        vis.add(frens)
            res += 1
        return 0    


# optimising adjacency list
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        if beginWord not in wordList:
            wordList.append(beginWord)

        adjList = {}
        # O(n)
        for w in wordList:
            # O(m)
            for i in range(len(w)):
                # O(m)
                temp = w[:i] + '*' + w[i+1:]
                if temp not in adjList:
                    adjList[temp] = [w]
                else:
                    adjList[temp].append(w)

        q = deque()
        res = 0
        vis = set()
        q.append(beginWord)
        # depth of tree
        while q:
            for i in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return res+1
                
                for i in range(len(w)):
                    key = w[:i] + '*' + w[i+1:]
                    for nbour in adjList[key]:
                        if nbour != w and nbour not in vis:
                            vis.add(nbour)
                            q.append(nbour)
            res += 1
        return 0

# O(v)
# while(graphTraversal.isEmpty == false)

#     currentVertex = graphTraversal.getVertex();

#     // This while loop will run Eaj times, where Eaj is number of adjacent edges to current vertex.
#     O(Eaj)
#     while(currentVertex.hasAdjacentVertices)
#         graphTraversal.add(adjacentVertex);

#     graphTraversal.remove(currentVertex);



s = Solution()
wl = ["hot","dot","dog","lot","log","cog"]
print(s.ladderLength("hit","cog",wl))
        




