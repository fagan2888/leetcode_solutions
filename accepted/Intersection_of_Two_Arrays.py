## https://leetcode.com/problems/intersection-of-two-arrays/

## looking to find numbers in common between two arrays (without
## having access to np.intersect1d, of course).  easiest way is to
## do a set intersection.  feels like cheating, but it's fast.

## ends up at 98th percentile for runtime but only 5th percentile
## for memory

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ## return as a list
        return list(set(nums1).intersection(nums2))