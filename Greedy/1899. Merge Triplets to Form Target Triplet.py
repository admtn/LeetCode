from typing import List
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # each index need to be present
        # its neighbours has to be equal or less than the target neigbhours
        solve = [0,0,0]
        for tri in triplets:
            for i in range(3):
                if tri[i] == target[i]:
                    if i == 0:
                        if tri[1] <= target[1] and tri[2] <= target[2]:
                            solve[0] = 1
                    elif i == 1:
                        if tri[0] <= target[0] and tri[2] <= target[2]:
                            solve[1] = 1
                    else: # i == 2
                        if tri[0] <= target[0] and tri[1] <= target[1]:
                            solve[2] = 1
                if sum(solve) == 3:
                    return True
        
        return sum(solve) == 3
    
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # each index need to be present
        # its neighbours has to be equal or less than the target neigbhours
        solve = [0,0,0]
        for tri in triplets:
            if tri[0] > target[0] or tri[1] > target[1] or tri[2] > target[2]:
                continue

            for i in range(3):
                if tri[i] == target[i]:
                    solve[i] = 1
            
            if sum(solve) == 3:
                return True
        
        return sum(solve) == 3