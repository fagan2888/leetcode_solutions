## https://leetcode.com/problems/single-number-ii/

## this is actually identical to single number III, but 
## we're just looking for a single number that exists 
## only once (instead of many numbera that exist only once),
## so we just return the 0th entry of the list.

## comes in at 52nd runtime percentile and 40th memory
## percentile

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for item in nums:
            count[item] = count.get(item, 0) + 1
        my_items = [i for i in count if count[i] == 1]
        return my_items[0]