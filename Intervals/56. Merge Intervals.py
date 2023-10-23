from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # have 2 pointers, compare left and right, if overlap then merge both, then shift both pointers right
        # if no overlap, append the left interval to res then move both pointers right.
        res = []
        if len(intervals) in [0,1]:
            return intervals
        intervals.sort()
        l = intervals[0]
        for i in range(1,len(intervals)):
            r = intervals[i]
            if not (l[1] < r[0] or l[0] > r[1]):
                l = [min(l[0],r[0]),max(l[1],r[1])]
            else:
                res.append(l)
                l = r
        res.append(l)
        return res


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        res.append(intervals[0])
        for st, end in intervals:
            if st <= res[-1][1]:
                res[-1][1] = max(end,res[-1][1])
            else:
                res.append([st,end])
        return res
