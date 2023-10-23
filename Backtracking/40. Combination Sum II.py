from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        candidates.sort()
        print(candidates)

        def backtrack(i,sum):
            if sum == target:
                result.append(subset.copy())
                return
            if sum > target or i == len(candidates):
                return
            
            
            #include
            subset.append(candidates[i])
            backtrack(i+1,sum+candidates[i])
            #don't include
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i+=1
            subset.pop()
            backtrack(i+1,sum)
        
        backtrack(0,0)
        return result
    
    # no point going down right subtree if left subtree terminates because it is too big or if it is equal , becaues right
    # is gonna get bigger

s = Solution()
ans = s.combinationSum2([1,2,2,3],5)
ans.sort()
print(ans)
