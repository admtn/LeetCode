from typing import List
from collections import defaultdict
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        def getDest(s, vis: defaultdict(int)):
            vis[s] = 0
            dist = 0
            cur = s
            while edges[cur] != -1 and edges[cur] not in vis:
                cur = edges[cur]
                dist += 1
                vis[cur] = dist
                
        d1, d2 = defaultdict(int), defaultdict(int)
        getDest(node1,d1)
        getDest(node2,d2)
        both = set(d1.keys()).intersection(set(d2.keys()))
        if len(both) == 0:
            return -1
        
        resNode, resDist = -1, float('inf')
        for n in both:
            if max(d1[n],d2[n]) < resDist or (max(d1[n],d2[n]) == resDist and n < resNode):
                resNode = n
                resDist = max(d1[n],d2[n])
        return resNode

print(Solution().closestMeetingNode([4,4,4,5,1,2,2],1,1))
