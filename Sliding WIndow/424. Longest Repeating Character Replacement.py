class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        alpha = {}
        l = 0
        r = 0
        maxf = 0
        alpha[s[0]] = 1
        while( r != len(s)-1):
            r+= 1
            alpha[s[r]] = alpha.get(s[r],0)+1
            maxf = max(maxf,alpha.get(s[r]))
            while(r - l + 1 - maxf > k):
                alpha[s[l]] -= 1
                l+=1

            res = max(res,r-l+1)

        return res