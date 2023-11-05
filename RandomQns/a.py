from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1

        while l <= r:
            m = (l+r)//2
            # if m in left sorted portion
            if nums[0] <= nums[m]:
                # if target in right sorted portion
                if target < nums[0]:
                    l = m+1
                # if target in left sorted portion, then do normal binary search
                elif target > nums[m]:
                    l = m+1
                elif target < nums[m]:
                    r = m-1
                else:
                    return m
            # if m in right sorted portion
            else:
                # target in left sorted postiion
                if target >= nums[0]:
                    r = m-1
                # target in right sorted position, then do normal binary search
                elif nums[m] > target:
                    r = m-1
                elif nums[m] < target:
                    l = m+1
                else:
                    return m
        return -1

print(Solution().search([5,1,3],5))