from typing import List
class Solution: # my goalpost soln
    def jump(self, nums: List[int]) -> int:
        end = len(nums)-1
        cache = {} # stores a number or False, if number == True ( number is min steps ) , so return 1 + min steps??
        cache[end] = 0
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= end:
                cache[i] = 1
            else:
                res = float('inf')
                for n in range(1,nums[i]+1):
                    if cache[i+n] != False:
                        res = min(res,1+cache[i+n])
            
                cache[i] = False if res == float('inf') else res
        
        return cache[0]

class Solution: # his bfs solution implemented by me
    def jump(self, nums: List[int]) -> int:
        cache = {}
        cache[0] = 0
        for i in range(len(nums)):
            for steps in range(1,nums[i]+1):
                if i+steps not in cache:
                    cache[i+steps] = cache[i] + 1
        return cache[len(nums)-1]
    
class Solution: # his bfs solution w his implementation
    def jump(self, nums: List[int]) -> int:
        l,r = 0,0
        res = 0
        while r < len(nums)-1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest, i+nums[i])
            l = r+1
            r = farthest
            res +=1
        
        return res