## https://leetcode.com/problems/sliding-window-median/

## this one is pretty easy for me, since it's pretty similar 
## to problems that I've solved for work :) 

## that said, to make it fast enough, I had to pull some tricks
## still doesn't end up all that fast -- would probably be better
## to use a binary tree or something like that to make insertion 
## and computing the median faster.

## ends up at 12th percentile for runtime and 69th percentile
## for memory, so could still be better.  technique is to keep
## a sorted list of the values we're going to median (relatively
## fast to do because we're only inserting 1 value and re-sorting 
## each time), then index that list.


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        from math import floor, ceil
        output_vals = len(nums)+1 - k
        
        vals_to_median = sorted(nums[:k])
        idx_to_add_next = k
        
        if k % 2 == 0:
            even = True
            upper_idx = int(k/2)
            lower_idx = upper_idx - 1
        else:
            even = False
            median_idx = int(floor(k/2))
        
        output = []
        for ii in range(output_vals):            
            if not even:
                output.append(float(vals_to_median[median_idx]))
            else:
                v = (vals_to_median[lower_idx] + vals_to_median[upper_idx])/2.0
                output.append(float(v))
            
            if idx_to_add_next > len(nums) - 1:
                break
            
            vals_to_median.remove(nums[ii])
            vals_to_median = sorted(vals_to_median + [nums[idx_to_add_next]])
            idx_to_add_next += 1
        
        return output