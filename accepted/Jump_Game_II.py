## https://leetcode.com/problems/jump-game-ii

# I have an advantage here, because I though a __lot__ about this problem
# to solve Jump Game I, and I can pretty easily adapt a non-optimal solution
# for that problem to this problem.  In particular, we'll put our jumper at
# the end of the array, have him/her move the maximum distance forward possible
# at each step, and figure out how many steps we take.  

# then, to get past a copule annoying worst-case cases, we do a bit of 
# optimization -- if all numbers are the same, then it's a trivial problem.

# coems in at 97th percentile for runtime and 6th percentile for memory.

# worst-case runtime complexity is still roughly O(n^2), which would be a 
# single 2 and a whole bunch of 1s.

class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return 0
        
        if len(set(nums)) == 1:
            ## all one number; can optimize this edge-case:
            return int((l-1)/nums[0])
        
        final_target = l-1
        jumper_loc = final_target

        njumps = 0
        while jumper_loc > 0:
            jumper_loc = min([ii for ii in range(jumper_loc) if (jumper_loc - ii <= nums[ii])])
            njumps = njumps + 1
        return njumps