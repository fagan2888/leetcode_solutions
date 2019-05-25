## https://leetcode.com/problems/max-increase-to-keep-city-skyline/

## given a grid that represents the height of buildings, find the total
## amount of height we can add to that grid without changing the skyline
## from any direction.

## effectively this boils down to finding the tallest building in each 
## row and column, then adding all the other buildings to match the shorter
## of the tallest building in their row or column

## that means that this is an O(2*N), where N is the number of grid 
## points -- first loop over the grid points finds the min/max of each
## column, second loop finds out how much we can add.

## comes in at 41st percentile in runtime and 12th in memory (because 
## of the dictionary, most likely)

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
         #gives the height of the building that sets the skyline of this row
        row_to_skyline = {} 

        #gives the height of the building that sets the skyline of this column
        column_to_skyline = {}  
        
        for row_index in range(len(grid)):
            row_to_skyline[row_index] = max(grid[row_index])
            for column_index in range(len(grid[row_index])):
                if row_index == 0:
                    column_to_skyline[column_index] = grid[row_index][column_index]
                else:
                    column_to_skyline[column_index] = max([column_to_skyline[column_index], grid[row_index][column_index]])
                    
        
        # ok, now I can just touch each square once more and figure out how much I can add        
        can_add = 0
        for row_index in range(len(grid)):
            skyline_of_row = row_to_skyline[row_index]
            for column_index in range(len(grid[row_index])):                
                skyline_of_column = column_to_skyline[column_index]
                min_height = min([skyline_of_row, skyline_of_column])
                can_add += min_height - grid[row_index][column_index]
        return can_add
            

