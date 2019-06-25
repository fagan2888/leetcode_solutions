## https://leetcode.com/problems/rotting-oranges

## this question really boils down to the question of finding the 
## shortest path from each fresh orange to each rotten orage.  I 
## do that by spawning walkers to sample every adjecent index from 
## each current walker (so long as that adjecent index has an orange
## and hasn't already been visited in the quest to rot this orange)
## until I land on a rotten one.  the answer is then the orange that's
## the furthest from a rotten one at the beginning.

## complexity is O(N) for the loop, but then the walkers can potentially
## require touching every index in the grid too (if there's a fresh orange
## in every square except the top left, which is rotten, then I'll have to
## touch every single orange on my way to the rotten one when finding the 
## path for the last fresh one).  I could speed it up by instituting a 
## memory for each orange -- once it's path is found, then any that land 
## on it necessarily have that path + the steps it took to get there as 
## option.  that means my worst-case scenario right now is O(N^2), where 
## N is the number of elements in the grid

## without that speedup I get 88th percentile runtime and 59th percentile 
## memory.  I took a quick stab at coding up that speedup and messed it up
## because you have to keep track of all possible paths then return the shortest
## at the end of the walkers, which means there's not actually a speedup 
## there (unless all walkers have hit a node with a path to rotten I guess...)

class Solution:
    def valid_neighbors(self, idx: tuple, visited: set) -> List[tuple]:
        return [(x, y) for (x, y) in [
            (idx[0]+1, idx[1]), 
            (idx[0]-1, idx[1]), 
            (idx[0], idx[1]+1), 
            (idx[0], idx[1]-1)] 
                if (
                    (x >= 0) and (x <= self.maxrow) and (y >= 0) and (y <= self.maxcol) 
                    and ((x, y) not in visited) and self.grid[x][y])]
    
    def path_to_rotten(self, idx: tuple) -> int:
        walkers = [idx]
        visited = {idx}
        steps = 0
        while True not in [self.grid[idx[0]][idx[1]]==2 for idx in walkers]:
            steps = steps + 1
            next_walkers = []
            for idx in walkers:
                visited.add(idx)
                next_walkers.extend(self.valid_neighbors(idx, visited))
            walkers = next_walkers
            if not len(walkers):
                return -1
        return steps
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.maxrow = len(grid)-1
        self.maxcol = len(grid[0])-1
                
        maxsteps = 0
        for rown, row in enumerate(grid):
            for coln, val in enumerate(row):
                if val == 1:
                    steps = self.path_to_rotten((rown, coln))
                    if steps == -1:
                        return -1
                    maxsteps = max(maxsteps, steps)
        return maxsteps