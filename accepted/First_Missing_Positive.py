## https://leetcode.com/problems/first-missing-positive

## we're looking for first missing positive integer in a 
## list of integers.  key insight is to realize that we 
## don't actually care about the numbers that __are__ in 
## the list; we only care about finding a positive integer
## that __is not__ in the list.  

## so, we turn nums into a set (allows and uses no extra memory) 
## then do an O(1) lookup for every positive integer until we find
## the one that we're missing.  that means our total best/worst-case 
## complexity is O(N)/O(2N).

## comes in at 99th percentile for runtime and 55th percentile
## for memory

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        maxval = len(nums)
        nums = set(nums)
        for n in range(1, maxval+3):
            if n not in nums:
                return n
            