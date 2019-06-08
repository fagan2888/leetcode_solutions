## https://leetcode.com/problems/reshape-the-matrix/

## problem is basicaly to implement np.array.reshape
## though of course we only have access to lists.

## relatively straightforward -- since we want to reshape
## in a row-access way, we just keep track of input and 
## output row numbers and column numbers and increment
## the two separately.

## surprisingly, this comes out to be 97th percentile
## in runtime and 30th percentil in memory.

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        nrows = len(nums)
        ncols = len(nums[0])
        osize = nrows*ncols
        nsize = r * c
        if osize != nsize:
            return nums
        
        colidx = 0
        rowidx = 0
        out = []
        for new_row_number in range(r):
            out.append([])
            for new_col_number in range(c):
                out[-1].append(nums[rowidx][colidx])
                colidx = colidx + 1
                if colidx == ncols:
                    colidx = 0
                    rowidx = rowidx + 1
        return out