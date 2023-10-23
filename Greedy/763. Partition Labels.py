from typing import List
from collections import defaultdict
class Ssolution:
    def partitionLabels(self, s: str) -> List[int]:
        def findLastChar(c):
            for i in range(len(s)-1,-1,-1):
                if s[i] == c:
                    return i
        
        segments = []
        segments.append(-1)
        vis = set()
        line = float('-inf')
        for i in range(len(s)):
            if s[i] not in vis:
                line = max(line,findLastChar(s[i]))
                vis.add(s[i])
            if i == line:
                segments.append(i)
        
        res = [segments[i]-segments[i-1] for i in range(1,len(segments))]
        return res

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        # indexes = defaultdict(list)
        indexes = {}
        for i in range(len(s)):
            if s[i] not in indexes:
                indexes[s[i]] = [i,i]
            else:
                indexes[s[i]][1] = i
        
        # print("dd")
        segments = []
        for c in indexes:
            # new segment (left outside, right outside)
            if len(segments) == 0:
                segments.append(indexes[c])
                continue
            if indexes[c][0] > segments[-1][1]:
                segments.append(indexes[c])
            elif indexes[c][1] < segments[-1][1]: # (both inside)
                continue
            else: # (left inside, right outside)
                segments[-1][1] = indexes[c][1]
        
        res = [i[1]-i[0]+1 for i in segments]
        return res

class NeetCodeSolution:
    def partitionLabels(self, s: str) -> List[int]:

        getLast = defaultdict(int)
        for i in range(len(s)):
            getLast[s[i]] = i
        
        size = 0
        end = 0
        res = []
        for i in range(len(s)):
            size += 1
            end = max(end,getLast[s[i]])
            if end == i:
                res.append(size)
                size = 0
        
        return res

        



s = Solution()
s.partitionLabels("faiokgeouingaqoeneqnagoiqngoqaue")