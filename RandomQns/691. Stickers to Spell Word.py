from typing import List
from collections import defaultdict
import heapq
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        target_set,sticker_set = set(),set()
        countC = defaultdict(int)
        for c in target:
            target_set.add(c)
            countC[c] += 1

        for w in stickers:
            for c in w:
                sticker_set.add(c)
        if target_set.difference(sticker_set):
            return -1
        
        def minus(word,dict:defaultdict):
            for c in word:
                if c in dict and dict[c] > 0:
                    dict[c] -= 1
                    if dict[c] == 0: dict.pop(c)
        cache = {}
        # dfs returns the min number of stickers to solve a given dict
        # O(2^n) time complexity, because for every char in target word, it can be present or absent.
        # 2 choices for n characters, so cache size is 2^n. 
        def dfs(dict:defaultdict):
            if sum(dict.values()) == 0:
                return 0
            if frozenset(dict.items()) in cache:
                return cache[frozenset(dict.items())]
            res = float('inf')
            for w in stickers:
                if list(dict.keys())[0] in w:
                    clone = dict.copy()
                    minus(w,clone)
                    res = min(res,dfs(clone))
            cache[frozenset(dict.items())] = res + 1
            return res + 1
        return dfs(countC)


            
print(Solution().minStickers(["these","guess","about","garden","him"],"atomher"))