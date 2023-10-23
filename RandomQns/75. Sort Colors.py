from typing import List
class sSolution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        color = 0
        while color < 3:
            for i in range(len(nums)):
                if nums[i] == color:
                    nums[idx],nums[i] = nums[i],nums[idx]
                    idx += 1
            color += 1
        print(nums)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r,m = 0,len(nums)-1,0
        while m <= r:
            if nums[m] == 0:
                nums[l],nums[m] = nums[m],nums[l]
                l += 1
                m += 1
            elif nums[m] == 2:
                nums[m],nums[r] = nums[r],nums[m]
                r -= 1
            else:
                m += 1
        print(nums)


Solution().sortColors([2,0,2,1,1,0])