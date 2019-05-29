## https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

## given a list that's already sorted, find the indices that bound
## a given element (or -1, -1 if that element is not in the list).
## goal is to this in O(log(n)), i.e. to take advantage of the fact
## that the list is sorted.  

## python's bisect library does this, so we can use bisect_left and
## bisect_right to solve this problem (i.e. do binary searches under
## the hood).  that solution comes in at 96th percentile in runtime and
## 83rd in terms of memory


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ## super base case -- no number in my list
        if not len(nums):
            return [-1, -1]
        
        ## slightly less base case -- is the number not in the list?
        if target < nums[0] or target > nums[-1]:
            return [-1, -1]
        
        ## otherwise, take advantage of the fact that it's sorted:
        import bisect
        
        l = bisect.bisect_left(nums, target)
        
        ## check if we found the number, or if we find the closest number
        if nums[l] != target:
            return [-1, -1]
        
        ## if we found the number itself, then bisect_right will find it too
        return [l, bisect.bisect_right(nums, target)-1]