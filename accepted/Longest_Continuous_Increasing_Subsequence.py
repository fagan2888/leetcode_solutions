## https://leetcode.com/problems/longest-continuous-increasing-subsequence/

## problem is to find the length of the longest continously increasing 
## subsequence.  solution is to loop through the sequence and keep track 
## of the length of the current sequence and the length of the longest
## sequence, then return the longest

## that means our complexity is just O(len(nums)); linear.

## comes in at 50th percentile for runtime and 37th for memory

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        long_length = 0
        cur_length = 1
        last_number_in_sequence = nums[0]

        larger = lambda x, y:  max([x, y])
        
        for ii in range(1, len(nums)):
            if nums[ii] > last_number_in_sequence:
                cur_length += 1
            else:
                long_length = larger(long_length, cur_length)
                cur_length = 1
            last_number_in_sequence = nums[ii]
            
        return larger(cur_length, long_length)
