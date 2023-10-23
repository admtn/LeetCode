from typing import List
from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1
        
        for number in dic:
            if dic[number] == 1:
                return number