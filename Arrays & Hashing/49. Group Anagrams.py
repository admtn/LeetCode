from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mapkey = defaultdict()
        for str in strs:
            key = [0] * 26
            for i in str:
                key[ord(i)-ord('a')] += 1
            key = tuple(key)
            mapkey[key].append(str)        
        return mapkey.values()



