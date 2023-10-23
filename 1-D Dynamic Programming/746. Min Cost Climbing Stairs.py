from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # from the goal, the cost of the last 2 steps will be the cost themselves.
        # from all other steps, the cost will be itself + min( 1step vs 2step )
        # n = num of steps
        n = len(cost)

        for i in range(n-3,-1,-1):
            cost[i] +=  + min(cost[i+1],cost[i+2])
        
        return min(cost[0],cost[1])
s = Solution()
print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))