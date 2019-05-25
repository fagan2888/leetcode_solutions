## https://leetcode.com/problems/contains-duplicate-iii/

## problem is to find whether a list of numbers contains
## nearly duplicate values, but those values are only allowed
## to be separated by a max of some number of spots in the list
## (i.e. the indices have to be close enough)...

## this (brute-force) solution is _almost_ fast enough, but 
## fails on the very last test-case.

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        ## t is the difference allowed between the indices
        ## k is the difference allowed between the values
        
        ## loop over each element of the list (except the last)
        for ii in range(len(nums)-1):

            ## loop over items within our allowed index range
            for jj in range(ii+1, ii+k+1):
                
                ## if we're beyond the end of the list, keep going
                if jj > len(nums)-1:
                    continue
                
                ## if we find a valid difference in this chunk, return True
                if abs(nums[ii] - nums[jj]) <= t:
                    return True
        
        ## if we got this far, then we didn't find any matches, so return False
        return False