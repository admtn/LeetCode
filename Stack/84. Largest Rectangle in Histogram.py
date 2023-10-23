from typing import List
class myRecursiveSoln:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        def getIndex(l,r):
            temp = float('inf')
            tempIndex = 0
            for i in range(l,r+1):
                if heights[i] < temp:
                    temp = heights[i]
                    tempIndex = i
            return tempIndex
        
        res = [0]
        def getArea(l,r):
            if r < l:
                return 0
            res[0] = max(res[0], min(heights[l:r+1])*(r-l+1))
            small_index = getIndex(l,r)
            getArea(l,small_index-1)
            getArea(small_index+1,r)
        getArea(0,len(heights)-1)
        return res[0]
    
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        last_index = len(heights) - 1
        for i in range(len(heights)):
            while len(stack) and heights[i] < stack[-1][1]:
                top_tuple = stack.pop()
                # length : if got things below me in stack, then his height is higher than mine
                # so length is the incoming index - his index - 1
                # area = length * height
                if len(stack):
                    area = (i-stack[-1][0]-1) * top_tuple[1]
                else:
                # if got nothing below me in stack, then my left bound goes all the way to the start of the list
                    area = i * top_tuple[1]
                res = max(res,area)
            stack.append((i,heights[i]))
        
        while len(stack) > 0 :
            temp = stack.pop()
            if len(stack) == 0:
                area = temp[1] * len(heights)
            else:
                area = temp[1] * (last_index - stack[-1][0])
            res = max(res,area)
        return res
s = Solution()
h = [2,1,5,6,2,3]
print(s.largestRectangleArea(h))