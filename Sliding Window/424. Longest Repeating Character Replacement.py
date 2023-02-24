class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        r = 0
        result = 0
        size = len(s)
        if(size == 0):
            return 0
        if(size == 1):
            return 1
        charSet.add(s[0])
        while( r != size-1 ):
            r+=1
            while(s[r] in charSet):
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            count = r-l+1
            result = max(result,count)

        return result