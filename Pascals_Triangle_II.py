## https://leetcode.com/problems/pascals-triangle-ii/
## comes in at 87th percentile in terms of runtime and 
## 66th percentile in terms of memory

## the runtime complexity of this solution is dominated by
## the inner list comprehension, since rowIndex is going to be
## small (< 33).  fortunately, python handles list comprehensions
## pretty well.  

## each row has N+1 cells, so the inner loop has complexity 
## O(rowIndex-2)

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ## base case:
        if rowIndex == 0:
            return [1]
        
        ## second row:
        current_row = [1, 1]        

        ## loop over remaining rows and sum up the previous row
        for ii in range(1, rowIndex):
            next_row = [1] + [current_row[j] + current_row[j+1] for j in range(len(current_row)-1)] + [1]
            current_row = next_row
        
        return current_row