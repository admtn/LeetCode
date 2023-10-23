from typing import List
from math import ceil
import heapq
class BinaryInsertion:

    def __init__(self):
        self.nums = []
        
    # find the smallest number that is bigger than num
    # binary insertion 
    # log(n) + n
    def addNum(self, num: int) -> None:
        l = 0
        r = len(self.nums)-1
        if len(self.nums) == 0 or num >= self.nums[r]:
            self.nums.append(num)
            return
        if num <= self.nums[0]:
            self.nums.insert(0,num)
            return
        
        while l <= r:
            m = ceil((l+r)/2)
            if num < self.nums[m]:
                r = m-1
                res = m
            elif num > self.nums[m]:
                l = m + 1
            else:
                self.nums.insert(m,num)
                return
        self.nums.insert(res,num)

    # O(1)
    def findMedian(self) -> float:
        i = len(self.nums)//2
        if len(self.nums)%2: # if odd
            return self.nums[i]
        else:
            return (self.nums[i] + self.nums[i-1])/2
        
class MedianFinder:

    def __init__(self):
        self.smallHeap = []
        self.bigHeap = []
    
    # maintain 2 heaps
    # diff in sizes <= 1
    # biggest val in small heap < smallest val in big heap
    # if any of these conditions are broken, pop biggest val from small heap and insert it into big heap.

    def addNum(self, num: int) -> None:
        s = self.smallHeap # maxHeap (-1)
        b = self.bigHeap # minHeap
        heapq.heappush(s,-num)

        if s and b and -s[0] > b[0]:
            val = heapq.heappop(s)
            heapq.heappush(b,-val)
        if len(s) - len(b) >= 2:
            val = heapq.heappop(s)
            heapq.heappush(b,-val)
        if len(b) - len(s) >= 2:
            val = heapq.heappop(b)
            heapq.heappush(s,-val)

    def findMedian(self) -> float:
        s = self.smallHeap # maxHeap (-1)
        b = self.bigHeap # minHeap
        if len(s) > len(b):
            return -s[0]
        elif len(b) > len(s):
            return b[0]
        else:
            return (-s[0]+b[0])/2



s = MedianFinder()
s.addNum(6)
print(s.findMedian())
s.addNum(10)
print(s.findMedian())
s.addNum(2)
print(s.findMedian())
s.addNum(6)
print(s.findMedian())
s.addNum(5)
print(s.findMedian())
s.addNum(0)
print(s.findMedian())
s.addNum(6)
s.addNum(3)
s.addNum(1)
s.addNum(0)
s.addNum(0)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()