from typing import List
class Solution:
    def climbStairs(self, n: int) -> int:
        combi = []
        subset = []

        def findCombis(sum):
            if sum == n:
                combi.append(subset.copy())
                return
            if sum > n:
                return

            subset.append(1)
            findCombis(sum+1)
            subset.pop()
            subset.append(2)
            findCombis(sum+2)

        findCombis(0)
        return len(combi)
    
s = Solution()
for i in range(1,11):
    print(f"{i} : {s.climbStairs(i)}")

