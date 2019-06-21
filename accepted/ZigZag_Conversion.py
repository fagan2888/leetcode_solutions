## https://leetcode.com/problems/zigzag-conversion/

## problem is to write a string in a zig-zag way across some number of 
## rows.  basically, I just keep track of whether I'm currently going up
## or down, and set my next row/col index accordingly, then join it all 
## together at the end. apparently there must be some kind of shortcut 
## to do this, since the brute-force solution is quite slow.  maybe it's 
## the way that I add columns -- should perhaps start with a longer set?

## tried that though, and didn't get a good speedup really.

## anyway, comes in at 7th percentile for speed and ~5th percentile for 
## memory.

class Solution:
    def add_column(self, matrix):
        for row in matrix:
            row.append('')
    
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        ## start with empty lists; add columns to each row as needed
        out_matrix = [['']*() for ii in range(numRows)]
        
        rowidx = 0
        colidx = 0
        going_down = True
        
        for char in s:
            r = out_matrix[rowidx]
            if len(r) <= colidx:
                self.add_column(out_matrix)
            
            r[colidx] = char
            
            if going_down:
                if rowidx == numRows - 1:
                    going_down = False
                    rowidx = rowidx - 1
                    colidx = colidx + 1
                else:
                    rowidx = rowidx + 1
            
            else:
                if rowidx == 0:
                    going_down = True
                    rowidx = rowidx + 1
                else:
                    rowidx = rowidx - 1
                    colidx = colidx + 1
        
        return ''.join([''.join(row) for row in out_matrix])