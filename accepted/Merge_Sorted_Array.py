## https://leetcode.com/problems/merge-sorted-array/

## this problem is marginally different from Merge Two Sorted
## Lists in that we want to do this in-place; i.e. we want to 
## move values from one array over to a second.

## I do this pseudo brute-force -- for each number in nums2, I
## iterate over the first list until I find a place it can go, 
## then shift all the entries from that spot down to the right
## one, then assign that spot.

## I take advantage of fact that nums2 is also sorted by keeping
## track of where I inserted the previous value from nums2, and 
## starting my search for the next value from there.

## that said, I still come in at only 29th percentile for runtime
## and 31st for memory.  worst-case complexity is not quite 
## O(n * m) because I don't iterate over all of n.  in fact, 
## I should only touch each number in nums1 once, which would make
## this O(n + m), I believe.

## however, there's also the step where we have to shift all 
## the values to the right -- that adds a fair bit of complexity
## unfortunately

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not n:
            return
        
        if m == 1 and n == 1:
            if nums2[0] < nums1[0]:
                nums1[1] = nums1[0]
                nums1[0] = nums2[0]
                return
            else:
                nums1[1] = nums2[0]
        
        n1idx = 0
        while len(nums2):
            n2val = nums2.pop(0)        
            for ii in range(n1idx, len(nums1)):
                if ii >= m:
                    ## are we into the empty space in the output array?
                    break                
                elif ii == len(nums1) - 1:
                    ## at the end, so we insert it last
                    break
                elif nums1[ii] > n2val:
                    ## found a place we can put the value
                    break

            ## now insert the value at ii, i.e. shift all other elements to the right
            for idx in reversed(range(ii, len(nums1))):
                nums1[idx] = nums1[idx-1]
            nums1[ii] = n2val
            
            ## search for the next val can start here
            n1idx = ii
            
            ## note that we've added a value to nums1 for the
            ## check of whether we're into the zeros
            m = m + 1