from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = [ gas[i] - cost[i] for i in range(len(gas))]
        if sum(res) < 0 :
            return -1
        
        cur = 0
        start = 0
        for i in range(len(res)):
            cur += res[i]
            if cur < 0:
                cur = 0
                start = i+1

        return start
    
    # intuition 
    # e.g
    # 1 2 5 -10 -3 4 5 -1 -2 -1 6
    # f  f f  f  f c ?  ?  ?  ? ?
    # f = failed, c = checking, ? = not checked
    # if 4 can reach the end of the array, we don't need to loop back because
    # 1. There is definitely a (unique) answer if sum(res) < 0. 
    # 2. so the answer has to be 4 or 5 or 6
    # 3. Since 4 can reach the end of the array, 4 is a better starting position then 5 and 6
    # (reaching the end of the array means that at no point in time did cur reach negative, meaning starting from)
    # (position 4 has brought a net positive as we move up along the res array)
    # (therefore since it brought a net positive, starting at a position LATER than 4 is going to bring LESS net positive)
    # ( so later positions are NOT better than 4.)
    # 4. Since the answer is unique, and 4 is better than 5 and 6, then 4 is the answer.
    # if at some point we travel along the res array and it was positive up until a certain point and became negative
    # just continue onto the next index from where it became negative +1 instead of where we started+1
    # because same reason as in brackets
    # if cur was positive all the way e.g starting from 1 > 2 > 5 then -10 caused it to become negative
    # no point checking 2 > 5 > -10 because 1 was positive all the way to -10 so 1 is better position than 2.

            
