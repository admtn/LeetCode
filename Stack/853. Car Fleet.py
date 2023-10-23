from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p,s in zip(position,speed)]
        pairs.sort(reverse=True)
        stack = []
        for o in pairs:
            # t = tar-pos/speed
            t = (target - o[0])/o[1]
            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
