## https://leetcode.com/problems/maximum-average-subarray-i/

## looking to find th elargest average of any kiven sub-array of
## nums that is of length k.  we can do that in O(N) if we use keep
## track of the current sum of our sub-array and the number we need 
## to next subtract.  then, each loop through just involves a 
## subtraction, an addition, a lookup, and a division -- O(n).

## still only hits 13th percentile in runtime and 15th percentile
## in memory.  could probably make it faster if I used a clever 
## list comprehension or something.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == k:
            return sum(nums)/k
        
        averages = []

        next_value_to_remove = nums[0]
        next_index_to_remove = 0
        current_sum = sum(nums[:k])
            
        for ii in range(k, len(nums)):
            averages.append(current_sum/k)
            
            ## remove the value at the beginning and add the next
            current_sum = current_sum - next_value_to_remove + nums[ii]
            next_index_to_remove = next_index_to_remove + 1
            next_value_to_remove = nums[next_index_to_remove]
        
        ## and now add on our final average from the last loop:
        averages.append(current_sum/k)
            
        return max(averages)