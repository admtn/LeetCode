from typing import List
class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) == 1:
            return 1
        nums3 = [0] * len(nums1)
        
        nums3[0] = min(nums1[0],nums2[0])
        for i in range(1,len(nums1)):
            if nums1[i] >= nums3[i-1] and nums2[i] < nums3[i-1]:
                nums3[i] = nums1[i]
            elif nums2[i] >= nums3[i-1] and nums1[i] < nums3[i-1]:
                nums3[i] = nums2[i]
            else:
                nums3[i] = min(nums1[i],nums2[i])
        nums3 = [0] * len(nums1)
        # increasing or same
        l,r = 0,1
        res = 1
        while r < len(nums3):
            if nums3[r] >= nums3[r-1]:
                res = max(res,r-l+1)
                r += 1
            else:
                l = r
                r += 1

        nums4 = [0] * len(nums1)
        for i in range(len(nums1)-1,-1,-1):
            if nums1[i] >= nums4[i-1] and nums2[i] < nums4[i-1]:
                nums4[i] = nums1[i]
            elif nums2[i] >= nums4[i-1] and nums1[i] < nums4[i-1]:
                nums4[i] = nums2[i]
            else:
                nums4[i] = min(nums1[i],nums2[i])
# [11,7,7,9]
# [19,19,1,7]

s = Solution()
s.maxNonDecreasingLength([1,3,2,1],[2,2,3,4])