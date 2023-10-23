from typing import List
class Ssolution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        for n in digits:
            res = res*10 + n
        res += 1
        ans = list(str(res))
        for i in range(len(ans)):
            ans[i] = int(ans[i])
        return ans

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        i = len(digits) - 1
        while c and i >= 0 :
            if digits[i] + 1 == 10:
                digits[i] = 0
                i -= 1
            else:
                digits[i] += 1
                c = 0
        if c:
            digits.insert(0,1)
        return digits

s = Solution()
print(s.plusOne([9]))