from typing import List
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        bucket = [[] for i in range(len(nums))] 
        for key in count:
            bucket[count[key]-1].append(key)
        
        res = [] 
        for i in range(len(bucket)-1,-1,-1):
            if len(res) == k:
                return res
            for number in bucket[i]:
                res.append(number)

        return res

s = Solution()
print(s.topKFrequent([1],1))