from typing import List
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        # are we in left or right?
        # if left
            # if target less than middle
                # if target less than L
                    # all nums left of l is bigger than target, so do l = m + 1
                # if target more than L
                    # that means target is between L and middle, so do r = m - 1
            # if target more than middle
                # l = m + 1
        # if right
            # if target less than middle
                # r = m - 1
            # if target more than middle
                # if target more than r
                    # r = m - 1
                # if target less than r
                    # l = m + 1
        while l <= r:
            m = (l+r)//2
            if nums[m] >= nums[0]:
                if target < nums[m]:
                    if target < nums[l]:
                        l = m + 1
                    else:
                        r = m - 1
                elif target > nums[m]:
                    l = m + 1
                else:
                    return m
            else:
                if target < nums[m]:
                    r = m - 1
                elif target > nums[m]:
                    if target > nums[r]:
                        r = m - 1
                    else:
                        l = m + 1
                else:
                    return m

s = Solution1()
print(s.search([1,3,5],1))
