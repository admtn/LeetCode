from typing import List
class mySolution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        # creates a list of prime numbers up to n
        # uses 2 pointer solution to find sum to target
        prime = []
        uptoN = [[i,True] for i in range(2,n+1)] # True is not crossed

        for i in range(len(uptoN)):
            if uptoN[i][1]:
                prime.append(uptoN[i][0])
                for j in range(i+uptoN[i][0],len(uptoN),uptoN[i][0]):
                    uptoN[j][1] = False
        
        l,r = 0,len(prime)-1
        res = []
        while l <= r:
            val = prime[l] + prime[r]
            if val < n:
                l += 1
            elif val > n:
                r -= 1
            else:
                res.append([prime[l],prime[r]])
                l += 1
                r -= 1
        return res
    
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


s = Solution()
print(s.findPrimePairs(10))


