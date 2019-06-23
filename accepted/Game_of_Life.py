## https://leetcode.com/problems/game-of-life

## problem is to take a single timestep in Conway's 
## game of life (see wikipedia), and to do it all in-place.
## I couldn't figure out a way to do inplace w/o two loops
## over the board, so this comes in at only 21st percentile
## for runtime (cause it's 2*O(n)), but it's 58th percentile
## for memory

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        maxrow = len(board)-1
        maxcol = len(board[0])-1

        ## use other number to represent intermediate states:
        # intermediate states:
        # -- currently alive, will become dead -> 1.5
        # -- currently alive, will stay alive -> 1
        # -- currently dead, will become alive -> 0.5
        # -- currently dead, will stay dead -> 0
        for rowidx in range(len(board)):
            for colidx in range(len(board[rowidx])):
                neighbors = [(rowidx+x, colidx+y) for x in [-1, 0, 1] for y in [-1, 0, 1] if (
                    (rowidx+x >= 0) and (rowidx+x <= maxrow) and (colidx+y >= 0) and (colidx+y <= maxcol)
                     and not (x==0 and y==0))]
                
                
                num_living_neighbors = sum([1 for (r, c) in neighbors if board[r][c] >= 1])
                living = board[rowidx][colidx] == 1
                if living:
                    ## leave living cells with 2-3 neighbors alive alone; all other become dead
                    if num_living_neighbors < 2 or num_living_neighbors > 3:
                        board[rowidx][colidx] = 1.5
                else:
                    if num_living_neighbors == 3:
                        board[rowidx][colidx] = 0.5
        
        ## now replace any 1.5s with 0 and 0.5s with 1
        for rowidx in range(len(board)):
            for colidx in range(len(board[0])):
                if board[rowidx][colidx] == 0.5:
                    board[rowidx][colidx] = 1
                elif board[rowidx][colidx] == 1.5:
                    board[rowidx][colidx] = 0
        
        # and now we're done