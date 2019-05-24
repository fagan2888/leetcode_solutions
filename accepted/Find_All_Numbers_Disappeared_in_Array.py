## https://leetcode.com/submissions/detail/230651834/

## problem is to find the numbers between 1 and length of the 
## array that aren't in the array.  simple way to do that is to
## do the set difference between range(1, len(ar)+1) and the 
## input numbers

## hits 98th percentile in terms of runtime, though only 
## 14th percentile in memory usage

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums)+1)) - set(nums))