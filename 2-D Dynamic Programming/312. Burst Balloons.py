from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache = {}
        nums.insert(0,1)
        nums.append(1)
        # dp returns max given l and r boundaries of list
        def dp(l,r):
            # if we reach the first balloon we gonna pop
            if l == r:
                return nums[l]*nums[l-1]*nums[r+1]
            if r < l:
                return 0
            
            if (l,r) in cache:
                return cache[(l,r)]
            
            soln = 0
            for i in range(l,r+1):
                soln = max(
                            soln,
                            nums[l-1]*nums[i]*nums[r+1] +
                            dp(i+1,r) +
                            dp(l,i-1)
                           )
            cache[(l,r)] = soln
            return soln
        return dp(1,len(nums)-2)

s = Solution()
print(s.maxCoins([1,2,3]))

