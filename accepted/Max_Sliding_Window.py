## https://leetcode.com/problems/sliding-window-maximum/submissions/

## problem:  find the max in each of the available length-k windows into 
## the array.  my straightforward solution -- use a list comprehension for
## speed.  requires multiple computations of maxes over very similar numbers
## though, so could be done better using a single loop over the array and updating 
## our max when we move the window off of the max or when we hit a larger number.

## this clearly suboptimal by the runtime (~19th percentile) and memory usage
## (27th percentile)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not len(nums):
            return []
        return [max(nums[ii:ii+k]) for ii in range(0, len(nums)-k+1)]