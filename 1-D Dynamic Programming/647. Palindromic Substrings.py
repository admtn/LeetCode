class Solution:
    def countSubstrings(self, s: str) -> int:

        def ceildiv(a,b):
            return -(-a//b)
        count = 0
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1

        return count

a = Solution()
b = a.countSubstrings("cbbd")
print(b)
