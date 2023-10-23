from typing import List
class mySolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        # soln dp list represents the max length of subsequence that ends with that number on the i'th index
        soln = [1] * len(nums)

        for i in range(1,len(nums)):
            for s in range(i-1,-1,-1):
                if nums[i] > nums[s]:
                    soln[i] = max(soln[i],soln[s]+1)
        
        return max(soln)

class topDown:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {i:None for i in range(len(nums))}
        # dfs returns the max length of sublist starting from index i
        def dfs(i):
            if i == len(nums)-1:
                return 1
            most_from_right = 0
            # find the longest we can get from starting with the i'th number, all numbers
            # on the right must be bigger than the i'th number. We get the numbers on the right 
            # by running dfs on them and getting the biggest value and storing it in most_from_right
            for s in range(i+1,len(nums)):
                if nums[i] < nums[s]:
                    if cache[s] == None:
                        cache[s] = dfs(s)
                    most_from_right = max(most_from_right,cache[s])
            
            # add one because we added the i'th number to the list (where list is the list from most from right)
            return most_from_right+1

        most = 0
        for i in range(len(nums)):
            if cache[i] == None:
                cache[i] = dfs(i)
            most = max(most,cache[i])

        return most
    
class bottomUp:
    # soln dp list represents the max length of subsequence that starts with that number on the i'th index
    def lengthOfLIS(self, nums: List[int]) -> int:
        soln = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i,len(nums)):
                if nums[i] < nums[j]:
                    soln[i] = max(soln[i],1+soln[j])
        
        return max(soln)



             
s = topDown()
a = s.lengthOfLIS([1,3,6,7,9,4,10,5,6])
# a = s.lengthOfLIS([10,6])
print(a)