## https://leetcode.com/problems/valid-mountain-array/

## we start off going up, then if we start going down 
## on the second value, if we hit a flat point, or if we
## start going up after we've gone down before, or if 
## we never start going down, then we've failed.

## comes in at 93rd percentile for run and 91st for memory

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        
        going_up = True
        prev = None
        for ii, val in enumerate(A):
            if prev is None:
                prev = val
            
            elif prev == val:
                return False
            
            elif prev < val:
                if going_up:
                    prev = val
                else:
                    return False
            else:
                ## i.e. prev > val
                if ii == 1:
                    return False
                prev = val
                going_up = False

        ## if we're still going up, then it's not a mountain
        return not going_up