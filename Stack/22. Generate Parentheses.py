from typing import List
from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # add left (condition : still got n)

        # add from pop (condition : stack got brackets)
        res = []
        stack = deque()
        def generate(string,brackets):
            if len(string) == 2 * n:
                res.append(string)
                return
            
            if brackets:
                stack.append(')')
                generate(string + '(', brackets-1)
                stack.pop()
            if len(stack) != 0:
                temp = stack.pop()
                generate(string + temp,brackets)
                stack.append(temp)
        
        generate("",n)
        return res

s = Solution()
print(s.generateParenthesis(3))

