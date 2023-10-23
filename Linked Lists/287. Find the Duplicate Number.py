from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast = 0,0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                break
        return slow
            
            
class pidgeonHole:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            cnt = 0
            for num in nums:
                if num <= i:
                    cnt += 1
            if cnt > i :
                return i
