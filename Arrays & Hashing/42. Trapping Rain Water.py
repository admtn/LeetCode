from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        lr = [0] * len(height)
        rl = [0] * len(height)

        curMax = 0
        for i in range(len(height)):
            if height[i] > curMax:
                curMax = height[i]
                lr[i] = height[i]
            else:
                lr[i] = curMax
        
        curMax = 0
        for i in range(len(height)-1,-1,-1):
            if height[i] > curMax:
                curMax = height[i]
                rl[i] = height[i]
            else:
                rl[i] = curMax
        
        res = [ min(lr[i],rl[i])-height[i] for i in range(len(height))]
        return sum(res)
class IterateOnce:
    def trap(self, height: List[int]) -> int:
        lr = [0] * len(height)
        rl = [0] * len(height)

        leftMax = 0
        rightMax = 0
    
        l = 0
        r = len(height) - 1

        for i in range(len(height)):
            leftMax = max(leftMax,height[l])
            lr[l] = leftMax
            rightMax = max(rightMax,height[r])
            rl[r] = rightMax
            l += 1
            r -= 1

        res = [ min(lr[i],rl[i])-height[i] for i in range(len(height))]
        return sum(res)
class ZeroMem:
    def trap(self, height: List[int]) -> int:
        leftMax = 0
        rightMax = 0
        l = 0
        r = len(height)-1
        res = 0
        while l<=r:
            if leftMax < rightMax:
                leftMax = max(leftMax,height[l])
                res += leftMax-height[l]
                l += 1
            else:
                rightMax = max(rightMax,height[r])
                res += rightMax-height[r]
                r -= 1
        
        return res

s = ZeroMem()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))