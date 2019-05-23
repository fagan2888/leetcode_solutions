## https://leetcode.com/problems/two-sum/

## shockingly, this dumb, brute-force solution is acceptable!  
## just do a double loop to make sure we touch all possible 
## combinations and add those combos to that have the right 
## sum to our final list.

## probably can do it faster with a list comprehension + filter,
## but the brute-force solution was accepted, so good enough for now.

## worst case run-time complexity is when the last two entries
## in the list sum up to my target, where the total runtime would
## be slightly better than O(N^2)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for ii in range(len(nums)):
            for jj in range(ii+1, len(nums)):
                if nums[ii]+nums[jj] == target:
                    return [ii, jj]