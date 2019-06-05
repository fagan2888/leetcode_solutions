## https://leetcode.com/problems/continuous-subarray-sum/

# this one was frustring because I missed the "of at least 
# size two" in the problem statement.  once I caught that, it
# became a lot lot easier to write.

# that said, this is a brute-force method

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ## if k < 0, then we can just set n negative, so set k positive
        k = abs(k)

        ## can get trues with k == 0, but also run risk of errors
        if k == 0:
            ## if k == 0, we'll get an error for x % k for all cases except 
            ## x == 0.  so, check if we have multiple zeros in a row.
            if True in [nums[ii] == nums[ii+1] == 0 for ii in range(len(nums)-1)]:
                return True
            else:
                return False

        for ii in range(len(nums)):
            s = nums[ii]
            for jj in range(ii+1, len(nums)):
                s = s + nums[jj]
                if s % k == 0:
                    return True
        
        return False