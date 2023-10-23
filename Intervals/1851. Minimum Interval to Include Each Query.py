from typing import List
import heapq
# class bruteForce:
#     def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
#         arr = [(i,i[1]-i[0]+1) for i in intervals]
#         arr.sort(key = lambda i:i[1])
#         output = []
#         for i,q in enumerate(queries):
#             for interval,size in arr:
#                 if self.inside(q,interval):
#                     output.append(size)
#                     break
#             if len(output) < i+1:
#                 output.append(-1)
#         return output
    
#     def inside(self,n,interval):
#         return n in range(interval[0],interval[1]+1)

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries = [(q,i) for i,q in enumerate(queries)]
        queries.sort(key = lambda i:i[0])
        minH,output = [],[0]*len(queries)
        i = 0
        for q,index in queries:
            while i < len(intervals) and q >= intervals[i][0]:
                heapq.heappush(minH,(intervals[i][1]-intervals[i][0]+1,intervals[i][1])) # push (length,end_val) into minH
                i += 1
            while minH and minH[0][1] < q: # pop all the intervals that are behind/not in range for the current query
                heapq.heappop(minH)
            output[index] = minH[0][0] if minH else -1
        return output
    
    # the idea here is to add all intervals that cur is ahead of, into our heap
    # then when we want to append the output for cur(query) , we pop heap until the end is equal or greater than cur
    # this ensures that cur is ahead of start and behind end, i.e cur is in range
    # since it is minheap, we will get the smallest val which is the answer.
    # we repeat the above loop as we iterate through the queries. (cur pointer moves)


s = Solution()
print(s.minInterval([[1,4],[2,4],[3,6],[4,4]],[2,3,4,5]))