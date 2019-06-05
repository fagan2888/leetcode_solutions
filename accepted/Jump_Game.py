## https://leetcode.com/problems/jump-game

## this one took me a minute to wrap my head around, 
## but once I happened on the solution, it was obvious:
## the only way in which we can't make it to the end is
## if there's a zero in the array somewhere (otherwise, 
## we can always keep moving forward).  If there is,
## then we have to check if we get stuck on that zero.
## if we do, then we return False; otherwise, we get to 
## the end and return True.

## worst-case complexity would O(n^2).  
## creating the set is O(n) + O(1) for lookup.  then,
## if there is a zero in the set, we have to jump.  if
## that zero is at the very beginning of an array that's
## made up of a whole bunch of 1s otherwise, then we'll
## have to walk our way back down to the very beginning
## step by step, and there's a check at each step of which 
## steps can get us there => O(n^2).  nonetheless, because
## the leetcode testcases have their pathologies at the 
## end, this ends up winning by a huge amount -- 
## 99.84th percentile in terms of runtime (though only 5th
## in terms of memory usage)

class Solution:    
    def canJump(self, nums: List[int]) -> bool:       
        ## if no zeros, can always get to the end
        if 0 not in set(nums):
            return True
        
        ## otherwise, find out if we get stuck at the zero(s) or if we can get past them
        ## start a jumper at the end, and have them make the max progress possible going
        ## backwards.  if we can get to the beginning, we're good.  otherwise, we get stuck
        ## at the zero and return False
        while jumper_loc > 0:
            can_get_to_me = [ii for ii in range(jumper_loc) if (jumper_loc - ii <= nums[ii])]
            if len(can_get_to_me) == 0:
                ## only way I can me here is to be here already!
                return False
            jumper_loc = min(can_get_to_me)
        return True