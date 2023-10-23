from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        total = len(nums1) + len(nums2)
        half = total//2

        A,B = nums1,nums2
        if len(A) > len(B):
            A,B = B,A
        # A is our smaller bottom array

        l,r = 0, len(A)-1
        while True:
            m = (l+r)//2
            top = half - m - 2

            Aleft = A[m] if m >= 0 else float('-inf')
            Aright = A[m+1] if m+1 < len(A) else float('inf')
            Bleft = B[top] if top >= 0 else float('-inf')
            Bright = B[top+1] if top+1 < len(B) else float('inf')

            if Aleft > Bright:
                r = m - 1
            elif Bleft > Aright:
                l = m + 1
            else:
                break

        if total%2: # odd
            return min(Aright,Bright)
        else: # even
            return (max(Aleft,Bleft)+min(Aright,Bright))/2
            

s = Solution()
# print(s.findMedianSortedArrays([4,5],[1,2,3]))
print(s.findMedianSortedArrays([],[1]))
            
