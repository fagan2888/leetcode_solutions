## https://leetcode.com/problems/find-peak-element/

## problem is to find any index where it's larger than 
## it's neighbors (with the ends taken to be -inf).

## do this brute force, since that only comes out to 
## O(n) in the worst case (if the peak is at the end
## of the array).  that is, add a -inf to each end of 
## the list, then iterate over it until we find what 
## we want.  honestly not sure why this is a medium 
## problem, but probably because there's a much faster
## way to do it -- my solution only comes in at 40th 
## percentile for runtime and 19th for memory (presumably
## because I add a couple elements to the list)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return nums.index(max(nums))
        
        
        from math import inf
        nums = [-inf] + nums + [-inf]

        ii = 1        
        while ii < len(nums) - 1:
            if nums[ii] > nums[ii-1] and nums[ii] > nums[ii+1]:
                break
            ii = ii + 1
        return ii-1