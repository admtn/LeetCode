from typing import List
import heapq
from collections import defaultdict
class FreqStack: 

    def __init__(self):
        self.hm = defaultdict(list)
        self.total = 0

    def push(self, val: int) -> None:
        self.total += 1
        if val in self.total:
            cnt,_ = self.hm[val]
            self.hm[val] = [cnt+1,self.total]
        else:
            self.hm[val] = [1,self.total]

    def pop(self) -> int:
        
# todo:
# how to get the next most frequent key?
# use queue, when we pop the most freq key, the next most freq key becomes next in the q
# 


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()