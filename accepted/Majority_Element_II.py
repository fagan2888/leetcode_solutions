## https://leetcode.com/problems/majority-element-ii/

## follow up to majority element, this time we're looking to find 
## all elements of an array that appear more than len(ar)/3 times.
## the challenge is to do this in O(n) time and O(1) space.

## my solution is to sort the list (O(log(N))), then loop over it (O(N))
## and keep track of the number of times the current item has appeared

## if it's more than n/3, we append it to a list of answers

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from math import floor
        
        nums.sort()
        to_return = []
        cur_val = None
        cur_count = 0
        
        crit_count = floor(len(nums)/3)
        
        for val in nums:
            if val == cur_val:
                cur_count += 1
            else:
                if cur_count > crit_count:
                    to_return.append(cur_val)
                    
                cur_count = 1
                cur_val = val
                
        if cur_count > crit_count:
            to_return.append(cur_val)
                
        return to_return