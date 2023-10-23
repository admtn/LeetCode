class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        
        # idea is to take each letter as a centre then expand outwards.
        for i in range(len(s)):
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]: # l cannot be 0, if it is 0 means at border so no need minus anymore. 
                l -= 1
                r += 1
  
            if r-l+1 > length:
                length = max(length,r-l+1)
                resl = l+1
                resr = r-1
            
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]: # l cannot be 0, if it is 0 means at border so no need minus anymore. 
                l -= 1
                r += 1
            
            if r-l+1 > length:
                length = max(length,r-l+1)
                resl = l+1
                resr = r-1
        
        return s[resl:resr+1:]
    
a = Solution()
b = a.longestPalindrome("cbbd")
print(b)

