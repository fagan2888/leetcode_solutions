## https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

## remove duplicates in-place such that no number appears more than 
## twice.  accomplish this by keeping track of what we're counting
## and what our count is at, and deleting items of the list (i.e.
## shifting the rest down) if we're above our allowed count of 2.

## O(n) runtime, and only 3 extra numbers (char, instances, and idx) 
## to keep track of otherwise => 99.8th percentile for runtime and 
## 57th for memory

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        counting_char = nums[0]
        instances = 1
        
        idx = 1
        while idx < len(nums):
            if nums[idx] == counting_char:
                instances = instances + 1
                if instances > 2:
                    del nums[idx]
                else:
                    idx = idx + 1
            else:
                counting_char = nums[idx]
                instances = 1
                idx = idx + 1
        return len(nums)