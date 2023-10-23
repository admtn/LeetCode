from typing import List
import heapq
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        def valid(s,b):
            return abs(s-b) <= limit
        
        minVals = deque() # increasing, get the next smallest value at head
        maxVals = deque() # decreasing, get the next biggest value at head
        l,r,res = 0,0,0
        while r < len(nums):
            while minVals and minVals[-1][0] >= nums[r]:
                minVals.pop()
            minVals.append((nums[r],r))

            while maxVals and maxVals[-1][0] <= nums[r]:
                maxVals.pop()
            maxVals.append((nums[r],r))

            if nums[r] == maxVals[0][0]: # if new number is a big number (max val)
                while not valid(minVals[0][0],maxVals[0][0]):
                    prev = minVals.popleft() # prev = (val,i)
                    l = prev[1] + 1
                while maxVals and maxVals[0][1] < l:
                    maxVals.popleft()
            else: # if new number is a small number (min val)
                while not valid(minVals[0][0],maxVals[0][0]):
                    prev = maxVals.popleft()
                    l = prev[1] + 1
                while minVals and minVals[0][1] < l:
                    minVals.popleft()
                
            res = max(res,r-l+1)
            r += 1

        return res

        
        # when we increase our window, we check if its valid
        # if invalid, check if our new number added is a min or max
        # if max
            # popleft from min queue/stack(monotonically increasting) to get the next smallest min and store popped val in prev
            # then check if the min[0] - max is valid, 
            # if valid move left pointer to prev min's i+1
            # if not valid, repeat.
            # based on the new l pointer, update the max deque such that max[0]'s i is >= l
        # if min
            # popleft from max queue/stack(monotonically decreasing) to get the next biggest max, and store it in prev
            # check if max[0] - min is valid
            # if valid, move left pointer to prev max's i+1
            # if not valid, repeat.
            # based on the new l pointer, update the min deque such that min[0]'s i >= l


class Cleaner:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        increasing = deque() # increasing, get the next smallest value at head
        decreasing = deque() # decreasing, get the next biggest value at head
        l,r,res = 0,0,0
        while r < len(nums):
            while increasing and increasing[-1] > nums[r]:
                increasing.pop()
            increasing.append(nums[r])

            while decreasing and decreasing[-1] < nums[r]:
                decreasing.pop()
            decreasing.append(nums[r])

            while increasing and decreasing and decreasing[0] - increasing[0] > limit:
                if nums[l] == decreasing[0]:
                    decreasing.popleft()
                if nums[l] == increasing[0]:
                    increasing.popleft()
                l += 1
            res = max(res,r-l+1)
            r += 1
        return res
        
        # when we increase our window, we check if its valid
        # if invalid, check if our new number added is a min or max
        # if max
            # popleft from min queue/stack(monotonically increasting) to get the next smallest min and store popped val in prev
            # then check if the min[0] - max is valid, 
            # if valid move left pointer to prev min's i+1
            # if not valid, repeat.
            # based on the new l pointer, update the max deque such that max[0]'s i is >= l
        # if min
            # popleft from max queue/stack(monotonically decreasing) to get the next biggest max, and store it in prev
            # check if max[0] - min is valid
            # if valid, move left pointer to prev max's i+1
            # if not valid, repeat.
            # based on the new l pointer, update the min deque such that min[0]'s i >= l

s = Cleaner()
li = [4,2,2,2,4,4,2,2]
print(s.longestSubarray(li,0))