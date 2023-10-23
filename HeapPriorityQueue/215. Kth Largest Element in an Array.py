from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        res = 0
        for i in range(k):
            res = heapq.heappop(nums)
        return -res
class qselect:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def quickSelect(l,r):
            pivot = nums[r]
            ptr = l
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[i], nums[ptr] = nums[ptr], nums[i]
                    ptr += 1
            nums[r], nums[ptr] = nums[ptr],nums[r]
            
            if k < ptr:
                return quickSelect(l,ptr-1)
            elif k > ptr:
                return quickSelect(ptr+1,r)
            else:
                return nums[ptr]
        
        return quickSelect(0,len(nums)-1)