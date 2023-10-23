from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        # 0 to 7, list
        # 2 to 9, actual
        # minus 2
        hash = [['a','b','c'],['d','e','f'],['g','h','i'],
                    ['j','k','l'],['m','n','o'],['p','q','r','s'],
                    ['t','u','v'],['w','x','y','z']]
        res = []
        cur = []
        def dfs(i):
            if i == len(digits):
                res.append(''.join(cur))
                return
            num = int(digits[i])
            for char in hash[num-2]:
                cur.append(char)
                dfs(i+1)
                cur.pop()
        dfs(0)
        return res

s = Solution()
print(s.letterCombinations("23"))

            
            
