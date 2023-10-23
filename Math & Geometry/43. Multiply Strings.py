from typing import List
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        if len(num1) < len(num2): # ensures num1 is the longer string
            num1, num2 = num2, num1
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i+j] += int(num1[i]) * int(num2[j])
        
        for i in range(len(res)):
            if res[i] >= 10:
                res[i+1] += res[i]//10
                res[i] %= 10
        
        resString = ""
        padding = True
        for i in range(len(res)-1,-1,-1):
            if res[i] != 0:
                padding = False
            if padding:
                continue
            resString += str(res[i])
        return resString

            

s = Solution()
s.multiply("123","456")        