from typing import List
class NumArray:
    def __init__(self, nums: List[int]):
        N = len(nums)
        self.nums = nums
        self.lr = [nums[0]] * N
        for i in range(1,N):
            self.lr[i] = nums[i] + self.lr[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.lr[right] - self.lr[left-1] if left else self.lr[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
