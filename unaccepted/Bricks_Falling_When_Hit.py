from functools import lru_cache

class Solution:
    def pretty_print(self):
        # print("Grid: ")
        print("="*len(self.grid[0]))
        for row in self.grid:
            print(' '.join([str(char) for char in row]))
        print("="*len(self.grid[0]))

    ## ok so the real meat of this problem is identifying when a brick
    ## drops.  let's write a function to solve that problem first:    
    @lru_cache(None)
    def does_brick_drop(self, row: int, col: int, checked_rows: str, checked_cols: str) -> bool:
        checked_indices = [[int(r), int(c)] for (r, c) in zip(checked_rows, checked_cols)]
        if row == 0:
            return False
        else:
            hold_cand_inds = [idx for idx in self.candidate_hold_neighbors([row, col]) if idx not in checked_indices]
            if not len(hold_cand_inds):
                return True
            checked_rows = checked_rows + str(row)
            checked_cols = checked_cols + str(col)
            for hold_cand in hold_cand_inds:
                if self.does_brick_drop(hold_cand[0], hold_cand[1], checked_rows, checked_cols) == False:
                    return False
                checked_rows = checked_rows + str(hold_cand[0])
                checked_cols = checked_cols + str(hold_cand[1])
            return True
                
    def same_row_neighbors(self, index: List[int]) -> List[List[int]]:
        row, col = index
        out = []
        if col > 0 and self.grid[row][col-1]:
            out.append([row, col-1])
        if col < self.maxcol and self.grid[row][col+1]:
            out.append([row, col+1])        
        return out
    
    def candidate_hold_neighbors(self, index: List[int]) -> List[List[int]]:
        row, col = index
        out = self.same_row_neighbors(index)
        if row > 0 and self.grid[row-1][col]:
            out.append([row-1, col])
        return out
        
    def candidate_drop_neighbors(self, index: List[int]) -> List[List[int]]:
        row, col = index
        out = self.same_row_neighbors(index)
        ## don't bother checking points that are already 0
        if row < self.maxrow and self.grid[row+1][col]:
            out.append([row+1, col])
        return out
    
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        ## ok so I can imagine a couple of high-level ways to solve this
        
        # 1) build a list of paths to the top for each brick in the 
        # intial grid, then anytime we delete or drop a brick, we just
        # have to check to see if any of the initial paths are now 
        # broken or, alternatively, iterate over all the paths and 
        # delete any that go through that brick.  then checking if a
        # a brick drops is trivial -- just ask if it has any paths 
        # remaining.
        
        # 2) check the entire grid each time...seems completely 
        # unnecessary
        
        # 3) check the blocks around the block we delete and chain 
        # reaction out from there -- probably the best way to go.
        
        ## unfortunately, while I think this is correct, it's still too
        ## slow...
        self.maxrow = len(grid) - 1
        self.maxcol = len(grid[0]) - 1
        self.grid = grid
                
        from collections import deque
        answer = []
        
        for hit in hits:
            row, col = hit
            if self.grid[row][col] == 0:
                ## if the block doesn't exist, nothing happens
                answer.append(0)
                continue

            ## set this grid point to 0 (delete it)
            self.grid[row][col] = 0
            
            ## now figure out what bricks get dropped...
            dropped = 0
            
            ## use a deque to work from the inside out
            drop_candidates = deque(self.candidate_drop_neighbors(hit))
            while len(drop_candidates):
                candidate = drop_candidates.popleft()
                cr, cc = candidate
                
                if not self.grid[cr][cc]:
                    ## did I already drop this one?
                    continue
                    
                # if self.does_brick_drop(candidate, checked_indices=[]):
                if self.does_brick_drop(cr, cc, '', ''):
                    ## drop the brick
                    self.grid[cr][cc] = 0
                    
                    ## note that we dropped the brick
                    dropped = dropped + 1
                    
                    ## check if this drop chain-reactions to it's neighbors (always moving out from the hit)
                    drop_candidates.extend(self.candidate_drop_neighbors(candidate))
                        
            answer.append(dropped)
            
            ## now we have to clear the cache because it's now wrong
            ## because of the checks against the grid
            self.does_brick_drop.cache_clear()
        return answer