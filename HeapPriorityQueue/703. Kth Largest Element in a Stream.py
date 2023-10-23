from typing import List
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
            heapq.heappush(self.nums,val)
            if len(self.nums) > self.k:
                heapq.heappop(self.nums)
            return self.nums[0]

s = KthLargest(1,[])
print(s.add(3))
print(s.add(5))
print(s.add(10))
print(s.add(9))
print(s.add(4))


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)