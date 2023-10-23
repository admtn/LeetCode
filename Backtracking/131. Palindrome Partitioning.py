from typing import List
import collections
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []
        cache = {}


        def palindrome(string):
            left = 0
            right = len(string)-1
            while(left < right):
                if string[left] == string[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True
        
        def getPartitions(i):
            
            if i >= len(s):
                res.append(subset.copy())
                return
            
            for end in range(i,len(s)):
                firstPartition = s[i:end+1]
                if cache.get(firstPartition,False):
                    subset.append(firstPartition)
                    getPartitions(end+1)
                    subset.pop()
                elif palindrome(firstPartition):
                    cache[firstPartition] = True
                    subset.append(firstPartition)
                    getPartitions(end+1)
                    subset.pop()

        
        getPartitions(0)
        return res

ob = Solution()
ans = ob.partition("aabb")
print(ans)