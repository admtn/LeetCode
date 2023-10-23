class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        def valid(s,b):
            return abs(s-b) <= limit
        
        increasing = deque() # increasing, get the next smallest value at head
        decreasing = deque() # decreasing, get the next biggest value at head
        l,r,res = 0,0,0
        while r < len(nums):
            while increasing and increasing[-1][0] >= nums[r]:
                increasing.pop()
            increasing.append((nums[r],r))

            while decreasing and decreasing[-1][0] <= nums[r]:
                decreasing.pop()
            decreasing.append((nums[r],r))

            if nums[r] == decreasing[0][0]: # if new number is a big number (max val)
                while not valid(increasing[0][0],decreasing[0][0]):
                    prev = increasing.popleft() # prev = (val,i)
                    l = prev[1] + 1
                while decreasing and decreasing[0][1] < l:
                    decreasing.popleft()
            else: # if new number is a small number (min val)
                while not valid(increasing[0][0],decreasing[0][0]):
                    prev = decreasing.popleft()
                    l = prev[1] + 1
                while increasing and increasing[0][1] < l:
                    increasing.popleft()
                
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