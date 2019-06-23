from functools import lru_cache
import itertools

## phew, proud of this one!  spent a lot of time thinking about it, 
## before realizing that I was failing not on the lookup but on the 
## creation of the table.  sped that up by switching to accumulated 
## sums (rather than summing up what's left), which is much much 
## faster.  So fast, in fact, that I got 100th percentile (44ms)!

## memory sucks though -- only 5th percentile.

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        # self.matrix = matrix
        self.sums_left_and_above = []
        nrows = len(self.matrix)
        self.maxrow = nrows - 1
        
        if self.maxrow >= 0:
            ncols = len(self.matrix[0])
            self.maxcol = ncols - 1
        else:
            self.maxcol = -1
            
        ### brute force is too slow -- need to pre-compute the sums and be able to look them up
        ## keep track of the sum to the left and above of each point for efficient lookups
        for rown, row in enumerate(matrix):
            if rown == 0:
                self.sums_left_and_above.append(list(itertools.accumulate(row)))
            else:
                row_above = self.sums_left_and_above[rown-1]
                rowsum = list(itertools.accumulate(row))
                self.sums_left_and_above.append([row_above[ii] + rowsum[ii] for ii in range(ncols)])

    @lru_cache(None)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        out = self.sums_left_and_above[row2][col2]
        if col1 != 0 and row1 != 0:
            ## remove region above row1 and to the left of col1, then add back on portion i double removed
            out = out - self.sums_left_and_above[row2][col1-1] - self.sums_left_and_above[row1-1][col2] + self.sums_left_and_above[row1-1][col1-1]
        
        elif col1 != 0:
            ## just remove to the left of col 1
            out = out - self.sums_left_and_above[row2][col1-1]
        
        elif row1 != 0:
            ## just remove above row 1
            out = out - self.sums_left_and_above[row1-1][col2]
 
        return out
            

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)