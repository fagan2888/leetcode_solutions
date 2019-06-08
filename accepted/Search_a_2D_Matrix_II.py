## https://leetcode.com/problems/search-a-2d-matrix-ii

## this one is identical to search_a_2d_matrix, but the matrix is 
## no longer sorted in the same way -- now, each item is smaller than
## the value below it and to it's right, but there no gaurantee of
## the relationship between those two values.  

## this problem is a great example of how you can overthink a problem 
## though.  here, the simple, brute-force approach (which doesn't take
## advantage of the sorting at all) is not only fast enough to be 
## accepted, but ends up in the 96th percentile for runtime and 50th for memory.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target in row:
                return True
        return False