from typing import List
from collections import deque
class Solution:
    def decodeString(self, s: str) -> str:
        st = deque()
        for i,c in enumerate(s):
            if c != ']':
                st.append(c)
            else:
                substr = ""
                while st[-1] != '[':
                    substr = st.pop() + substr
                st.pop()
                k = ""
                while st and st[-1].isdigit():
                    k = st.pop() + k
                st.append(int(k)*substr)
        return "".join(st)

                
        
print(Solution().decodeString("3[a]2[bc]"))