## https://leetcode.com/problems/image-smoother/

## problem is to smooth an image by averaging each pixel over 
## it's neighbors.  this solution is hardly optimal (comes in 
## at only 14th percentile in terms of runtime, but it's accepted
## and relatively easy to understand.  for non-base cases (explained
## below), we add each pixel's value to itself and all of it's neighbors,
## then do a second pass to do all the division.  should probably 
## eliminate that second pass to optimize.  total complexity for 
## non-base cases is O((nrows * ncols)^2), I believe

class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        from math import floor
        import itertools
        nrows = len(M)
        ncols = len(M[0])
                
        last_row_index = nrows - 1
        last_col_index = ncols - 1


        ## base cases:

        ## single pixel image -- no smoothing
        if nrows == 1 and ncols == 1:
            return M

        ## single row image -- left-right smoothing only
        elif nrows == 1 and ncols > 1:
            answer_row = [floor((M[0][0]+M[0][1])/2)]
            for jj in range(1, ncols-1):
                answer_row.append(floor(sum([M[0][jj-1], M[0][jj], M[0][jj+1]])/3.0))
            answer_row.append(floor((M[0][-2]+M[0][-1])/2))
            return [answer_row]

        ## single column image -- top/bottom smoothing only
        elif nrows > 1 and ncols == 1:
            answer = [[floor((M[0][0]+M[1][0])/2)]]
            for jj in range(1, nrows-1):
                answer.append([floor(sum([M[jj-1][0], M[jj][0], M[jj+1][0]])/3.0)])
            answer.append([floor((M[-2][0]+M[-1][0])/2)])
            return answer
            
        ## create an output array to hold our sums
        sums = []
        for ii in range(nrows):
            sums.append([0 for jj in range(ncols)])
        
        ## figure out the number of neighbors each pixel has
        num_divisors_top_bottom = [4] + [6]*(ncols-2) + [4]
        num_divisors_middle = [6] + [9]*(ncols-2) + [6]
        
        num_divisors = [num_divisors_top_bottom]
        for ii in range(nrows-2):
            num_divisors.append(num_divisors_middle)
        num_divisors.append(num_divisors_top_bottom)
        

        ## filtering functions to eliminate invalid neighbor indices
        valid_row_check = lambda x:  x >= 0 and x <= last_row_index
        valid_col_check = lambda x:  x >= 0 and x <= last_col_index
        
        ## loop over rows:
        for ii in range(nrows):            
            # loop over columns
            for jj in range(ncols):
                ## build a list of the rows & columns above me, me, and below me that exist
                neighbor_rows = list(filter(valid_row_check, [ii-1, ii, ii+1]))
                neighbor_cols = list(filter(valid_col_check, [jj-1, jj, jj+1]))

                ## take the product of those two lists (i.e. (x1, y1), (x1, y2), ...(x3, y1), ...)
                ## which forms the indices of my neighbors (and myself)
                for (row_idx, col_idx) in list(itertools.product(neighbor_rows, neighbor_cols)):
                    ## add my value to all my neighbors
                    sums[row_idx][col_idx] = sums[row_idx][col_idx] + M[ii][jj]
        
        ## on reflection, this loop is completely unnecessary, as the division 
        ## can be subsumed into the above operations, which would also eliminate the 
        ## need for a second copy of the image.

        ## anyway, here we're going to loop over the rows and do a list comprehension to 
        ## do the division over the columns
        answer = []
        for ii in range(nrows):
            answer.append([floor(sums[ii][jj]/num_divisors[ii][jj]) for jj in range(ncols)])
        
        return answer