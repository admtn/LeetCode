from typing import List
class TopDown:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = { i:None for i in range(len(s)) }
        def f(i):
            if i == len(s):
                return True
            if cache[i] != None: return cache[i]
            for word in wordDict:
                n = len(word)
                remainder = s[i:i+n]
                if remainder == word:
                    if f(i+n): 
                        return True
                    else: 
                        cache[i+n] = False
            return False
                
        
        return f(0)
# check each word in dict from the start of the i-th letter and compare if same.
class BottomUp:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        soln = [None] * (n+1)
        soln[n] = True
        for i in range(n-1,-1,-1):
            for word in wordDict:
                if word == s[i:i+len(word)] and soln[i+len(word)]:
                    soln[i] = soln[i+len(word)]
                    break
                
                soln[i] = False
        
        return soln[0]

class Redo:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        # dfs checks whether a word can be solved starting from index i
        def dfs(i):
            if i == len(s):
                return True
            if i in cache: return cache[i]
            for w in wordDict:
                if w == s[i:i+len(w)]:
                    if dfs(i+len(w)): return True
            cache[i] = False
            return False
        
        return dfs(0)


s = BottomUp()
ans = s.wordBreak("abcd",["a","abc","b","cd"])
print(ans)

# s = TopDown()
# ans = s.wordBreak("cars",["car","ca","rs"])
# print(ans)