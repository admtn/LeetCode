from typing import List
class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        prime = [True for i in range(n+1)]
        for i in range(2,n+1):
            if prime[i]:
                for j in range(2*i,n+1,i):
                    prime[j] = False
        
        res = []
        for i in range(2,n+1):
            if i > n-i:
                break
            if prime[i] and prime[n-i]:
                res.append([i,n-i])
        
        return res