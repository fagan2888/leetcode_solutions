## https://leetcode.com/problems/set-matrix-zeroes/

## again not positive why this is a medium problem.  simple solution works
## fine -- do two passes over the array and keep track of the column and 
## row indices (w/ a set, but could also do a list) that I need to zero on
## a second pass over just those indices

## comes in at ~98th percentile for runtime and ~97th percentile for 
## memory, so apparently this simple solution is more than good enough

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ## do this in two passes -- first pass builds a set of the rows & columns I will zero, 
        ## second pass does the zeroing
        cols_to_zero = set([])
        rows_to_zero = set([])
        for rowidx, row in enumerate(matrix):
            ## only need to bother operating on rows that have zeros in them
            if 0 in row:
                rows_to_zero.add(rowidx)
                cols_to_zero |= {idx for idx in range(len(row)) if not row[idx]}

        for rowidx in rows_to_zero:
            matrix[rowidx] = [0]*len(matrix[rowidx])
        for colidx in cols_to_zero:
            for rowidx in range(len(matrix)):
                matrix[rowidx][colidx] = 0