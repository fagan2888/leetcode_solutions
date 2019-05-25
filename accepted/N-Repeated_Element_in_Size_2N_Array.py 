## https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

## find the element of an array that is repeated N times (in a len 2N 
## array).  sort the elements (O(log(N))), then iterate over them (O(N)
## at worst, if our answer is the largest element in the array) and
## keep track of how many of the same element we've hit so far, then 
## return once we hit enough.  

## probably some simple trick to do this a lot faster with itertools.groupby

## comes in at only 20th percentile in runtime but 53rd in memory


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        A.sort()
        last_v = None
        counter = 0
        target = int(len(A)/2)
        for v in A:
            if v == last_v:
                counter = counter + 1
                if counter == target:
                    return v
            else:
                last_v = v
                counter = 1
        ## if we got here, then the largest element in the array 
        ## is our answer (since we're guaranteed to have an answer
        ## according to the problem statement)
        return v
                