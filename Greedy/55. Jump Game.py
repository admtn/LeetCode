from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        cache = {}
        def dfs(i):
            if i == goal:
                return True
            if i > goal:
                return False
            if i in cache:
                return cache[i]
            for steps in range(nums[i]+1,0,-1):
                if dfs(i+steps):
                    return True
            cache[i] = False
            return False
        return dfs(0)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= goal:
                goal = i

        return True if not goal else False
