from typing import List
from math import ceil
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # 1  2  3  4  5* 6* 7* 8*
        # 1  8* 2  7* 3  6* 4  5* 
        nums.sort()
        N = len(nums)
        res = []
        for i in range(ceil(N/2)):
            res.append(nums[i])
            if i != N-i-1:
                res.append(nums[N-i-1])
        return res

print(Solution().rearrangeArray([1,2,3,4]))