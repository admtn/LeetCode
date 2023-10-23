class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        N = len(s)
        left_1s, right_0s = [0] * (N+1) , [0] * (N+1)
        one,zero = 0,0
        for i in range(N):
            if s[i] == '1':
                one += 1
            left_1s[i+1] = one
        
        for i in range(N-1,-1,-1):
            if s[i] == '0':
                zero += 1
            right_0s[i] = zero
        
        res = float('inf')
        for i in range(N+1):
            res = min(res, left_1s[i]+right_0s[i])
        return res

print(Solution().minFlipsMonoIncr("011010"))