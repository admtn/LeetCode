from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # take the left of l insertion, if none , it will be itself
        # take right of r insertion, if none, it will be itself
        # get all the lists to the left of the index and all the lists to the right of the index
        st, ed = newInterval[0],newInterval[1]
        for i in range(len(intervals)):
            for j in intervals:
                if st <= intervals[j]:
                    if j == 0: # if outside window
                        leftPt = i
                    else:
                        leftPt = i
                        


        

