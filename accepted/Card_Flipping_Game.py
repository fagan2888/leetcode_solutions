## https://leetcode.com/problems/card-flipping-game/

## this problem comes down to finding the smallest number
## that we can put on the back of a card without putting 
## that same number on the frong.  i do this by finding all
## invalid numbers, then taking the minimum of the remaining
## numbers.  invalid numbers are those that appear on the
## front and back of the same car.

## complexity is roughly O(len(fronts))

## comes in at 99th percentile in terms of runtime, though
## only 31st in terms of memory

class Solution:    
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        ### basically, looking to get the smallest number on the back 
        ## that's not on a front
        ## numbers that are on both the front and back of a single card 
        ## can be instantly eliminated
        ## all other numbers are valid -- there's sure to be a way to isolate 
        ## each on the backs only
        invalid_nums = set(fronts[ii] for ii in range(len(fronts)) if fronts[ii] == backs[ii])
        all_numbers = set(fronts+backs)
        valid_numbers = list(all_numbers.difference(invalid_nums))

        if not len(valid_numbers):
            return 0
        return min(valid_numbers)
        
        
        