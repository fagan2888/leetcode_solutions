## https://leetcode.com/problems/search-a-2d-matrix

## problem is to check whether a number is in a 2D matrix,
## where the matrix is sorted (or would be if we were to 
## flatten it).  My solution is to iterate over the rows, 
## comparing to just the last value, until we find a row 
## with a last value <= our target, whcih implies that our
## target must be in the row that we just touched or not 
## be in the matrix at all.

## so then it's a simple target in that row.

## runtime is 81st percentile and memory is 49th percentile.


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## ok, so it's a sorted matrix...
        if not len(matrix):
            return False
        if not len(matrix[0]):
            return False
        
        rown = 0
        while rown < len(matrix)-1 and target > matrix[rown][-1]:
            rown = rown + 1            
        return target in matrix[rown]