from typing import List
import heapq



class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        minHeap = []
        intervals.sort(key = lambda intervals:(intervals.start,intervals.end))
        res = 0
        for meeting in intervals:
            st,end = meeting.start, meeting.end
            while minHeap and st >= minHeap[0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap,end)
            res = max(res,len(minHeap))
        return res

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        minHeap = []
        intervals.sort(key = lambda intervals:(intervals.start,intervals.end))
        res = 0
        # n
        for meeting in intervals:
            st,end = meeting.start, meeting.end
            # n log n (technically is log n because the max num.of times we will pop is n times, i.e if for each iteration in of intervals
            # we pop once, we will have popped the exact amount of times we would need to pop)
            while minHeap and st >= minHeap[0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap,end)
            res = max(res,len(minHeap))
        return res
        # nlogn

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # We have 2 arrays , start and end
        # We will look at the smaller one, if smaller one is st, increment cur and update res, shift st pointer 
        # if smaller one is end, decrement cur, shift end pointer
        # if same, then decrement cur.
        st = [i.start for i in intervals]
        st.sort()
        end = [i.end for i in intervals]
        end.sort()
        cur,res,s,e = 0,0,0,0
        while s < len(st):
            if st[s] < end[e]:
                cur += 1
                res = max(res,cur)
                s += 1
            else: # if end is smaller or same
                cur -= 1
                e += 1 # to do : out of bounds
        return res
        


s = Solution()
li = [Interval(5,8),Interval(6,8)]
print(s.min_meeting_rooms(li))
