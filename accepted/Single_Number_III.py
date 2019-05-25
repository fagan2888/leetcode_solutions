## https://leetcode.com/problems/single-number-iii/

## problem is to find the subset of numbers in nums
## that appear only once.  build up a dictionary via
## a single loop through the list, then pull out all 
## the items in the dictionary of counts that appeared
## only once.  runtime is dominated by loop over the 
## numbers, so O(N)...

## comes in at 73rd percentile in runtime and and 27th
## percentile in terms of memory

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = {}
        for item in nums:
            count[item] = count.get(item, 0) + 1
        my_items = [i for i in count if count[i] == 1]
        return my_items