## https://leetcode.com/problems/cherry-pickup/submissions/

## I thought this was a pretty clever solution that's nice and readable, but
## it's not even close to being fast enough -- crashes on just the 5th (of 64)
## test case

class Solution:
    class Walker:
        def __init__(self, row: int, col: int, picked: int, visited: set):
            self.row = row
            self.col = col
            self.picked = picked
            self.visited = visited

        def reached_end(self, maxrow: int, maxcol: int) -> bool:
            return self.row == maxrow and self.col == maxcol

        def is_finished(self) -> bool:
            return self.row == 0 and self.col == 0

        def available_down_steps(self, grid: List[List[int]], maxrow: int, maxcol: int) -> List[List[int]]:
            possible_next = []
            if self.row < maxrow and grid[self.row+1][self.col] >= 0:
                possible_next.append([self.row+1, self.col])

            if self.col < maxcol and grid[self.row][self.col+1] >= 0:
                possible_next.append([self.row, self.col+1])
            return possible_next

        def available_up_steps(self, grid: List[List[int]]) -> List[List[int]]:
            possible_next = []
            if self.row > 0 and grid[self.row-1][self.col] >= 0:
                possible_next.append([self.row-1, self.col])

            if self.col > 0 and grid[self.row][self.col-1] >= 0:
                possible_next.append([self.row, self.col-1])

            return possible_next

    
    def cherryPickup(self, grid: List[List[int]]) -> int:
        walkers = [self.Walker(0, 0, 0, set([]))]
        reached_end = []
        max_picked = 0
        
        maxrow = len(grid)-1
        maxcol = len(grid[0])-1
        
        while len(walkers):
            next_walkers = []
            for walker in walkers:
                if grid[walker.row][walker.col] == 1:
                    ## don't need to do the visited check here...
                    walker.picked += 1
                    
                    ## only bother keeping track of the tuples that had cherries
                    walker.visited = walker.visited.union({(walker.row, walker.col)})
                    
                next_options = walker.available_down_steps(grid, maxrow, maxcol)
                if not len(next_options):
                    if walker.reached_end(maxrow, maxcol):             
                        reached_end.append(walker)
                else:
                    next_walkers += [self.Walker(n[0], n[1], walker.picked, walker.visited) for n in next_options]
            walkers = next_walkers
            
        # print(f"{len(reached_end)} walkers made it to the end")
        # for w in reached_end:
        #     print(w.picked, w.visited)
        ## now walk back up...
        walkers = reached_end
        while len(walkers):
            next_walkers = []
            for walker in walkers:
                if grid[walker.row][walker.col] == 1 and (walker.row, walker.col) not in walker.visited:
                    walker.picked += 1
                ## no need to add to my set of visited points on the way back up
                next_options = walker.available_up_steps(grid)
                if not len(next_options):
                    if walker.is_finished():
                        max_picked = max(max_picked, walker.picked)
                else:
                    next_walkers += [self.Walker(n[0], n[1], walker.picked, walker.visited) for n in next_options]
            walkers = next_walkers
        return max_picked