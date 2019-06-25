## https://leetcode.com/problems/find-the-duplicate-number

## this one is slightly different from the previous one, which
## asked me to find both a duplicated and missing number.  finding
## just the duplicate one is easy -- build a set of my previous 
## items (O(1) lookup), then return whenever I hit the duplicate.

## runtime is 94th percentile; memory is 16th percentile.

## complexity:  O(2*N) -- both the lookup and the add are O(1), so 
## it's effectively 2 operations per item until I hit the duplicate
## item.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        past = set([])
        for n in nums:
            if n in past:
                return n
            else:
                past.add(n)