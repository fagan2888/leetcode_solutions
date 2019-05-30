## 

## problem is to determine whether a given sudoku board 
## is valid or not.  that boils down to checking for duplicates
## in each row, column, and 3x3 square.

## a little bit of cheating/hardcoding here to 9x9 boards, since
## I define the square indices by hand because I'm not feeling well.

## runtime complexity here is O(9 + 9 + 9), since we have 9 rows, 
## 9 columns, and 9 squares.  the validation is pretty quick since 
## we use a filter to get rid of the '.'s and then just check the 
## length against that of a set for uniqueness/repeated numbers.

## indeed, comes in at 93rd percentile for runtime and 79th percentile
## for memory.

class Solution:
    def validate_sequence(self, sequence:  List[str]) -> bool:
        nums = [n for n in sequence if n != '.']
        unums = set(nums)
        ## check if all are unique:
        if len(unums) != len(nums): 
            return False
        else:
            return True
        
    
    def validate_rows(self, board: List[List[str]]) -> bool:
        ## this one is easy:
        for row in board:
            if not self.validate_sequence(row):
                return False
        return True
            
    def validate_columns(self, board:  List[List[str]]) -> bool:
        ## this one is slightly harder, but not much
        for coln in range(len(board[0])):
            column = [row[coln] for row in board]
            if not self.validate_sequence(column):
                return False
        return True
    
    def validate_squares(self, board:  List[List[str]]) -> bool:
        # import itertools
        ## ok this is the hard one
        ## have to index the squares...
        
         ## ii is my square number; not actually related to row/column
            ## ii = 0 => rows 0-2 :: cols 0-2
            ## ii = 1 => rows 0-2 :: cols 3-5
            ## ii = 2 => rows 0-2 :: cols 6-8
            ## ii = 3 => rows 3-5 :: cols 0-2
            ## ...
                    
        row_indices = {0:[0, 1, 2], 1:[0, 1, 2], 2:[0, 1, 2],
                       3:[3, 4, 5], 4:[3, 4, 5], 5:[3, 4, 5],
                       6:[6, 7, 8], 7:[6, 7, 8], 8:[6, 7, 8]}
        
        col_indices = {0:[0, 1, 2], 3:[0, 1, 2], 6:[0, 1, 2],
                       1:[3, 4, 5], 4:[3, 4, 5], 7:[3, 4, 5],
                       2:[6, 7, 8], 5:[6, 7, 8], 8:[6, 7, 8]}        
        
        for ii in range(len(board)):
            my_rows = row_indices[ii]
            my_cols = col_indices[ii]
            
            seq = [board[rown][coln] for rown in my_rows for coln in my_cols]
            if not self.validate_sequence(seq):
                return False
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not self.validate_rows(board):
            return False
        
        if not self.validate_columns(board):
            return False
        
        if not self.validate_squares(board):
            return False
        
        return True