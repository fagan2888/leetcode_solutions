## https://leetcode.com/problems/median-of-two-sorted-arrays/

## almost feels like cheating since python's standard library 
## provides a way to merge two sorted lists using heaps under
## the hood, so we do that then figure out where to index to 
## get our median.

## comes in at 64th percentile in runtime and 61st percentile
## in memory


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        from heapq import merge
        merged = list(merge(nums1, nums2))
        tot_len = len(merged)
        if tot_len % 2 == 0:
            ## even lengthed list; average of the two middle values
            idx = int(tot_len / 2)
            return (merged[idx]+merged[idx-1])/2.0
        else:
            ## odd length list; just the middle value
            idx = int(tot_len / 2)
            return 1.0*merged[idx]