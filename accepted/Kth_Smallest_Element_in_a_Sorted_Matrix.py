## https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

## given an n x n matrix where each row and column is sorted (but row_i[-1] is
## not necessarily < row_{i+1}[0]), find the kth smallest element.

## shockingly, the brute-force approach is accepted, though just barely

## we accomplish this by inserting each row into the total list in a way 
## that's optimized to insert one sorted list into another (note -- this 
## would come in handy in some other problems too!).  this gives us 
## only ~7th percential in terms of runtime and ~14th in terms of RAM.

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import bisect
        values = matrix[0]
        for row in matrix[1:]:
            for val in row:
                bisect.insort(values, val)

        return values[k-1]