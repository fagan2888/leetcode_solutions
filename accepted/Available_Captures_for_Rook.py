## https://leetcode.com/problems/available-captures-for-rook/

## this is an easy one, if annoying because I didn't bother 
## writing a function so I have to do all 4 checks separately.

## solution comes in at 93rd percentile for runtime and 44th 
## for memory

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        from copy import deepcopy
        
        ## first, where is our rook?
        rook_row_idx = ['R' in row for row in board].index(True)
        rook_row = board[rook_row_idx]
        
        rook_col_idx = [val=='R' for val in rook_row].index(True)
        rook_col = [row[rook_col_idx] for row in board]
        
        captures = 0
        
        ## now iterate until I find either a p or a B, or I hit the end of the board
        ## should refactor this into a function, but meh
        above_row_idx = deepcopy(rook_row_idx)
        while above_row_idx > 0 and rook_col[above_row_idx] in ['.', 'R']:
            above_row_idx -= 1            
        if rook_col[above_row_idx] == 'p':
            captures += 1
        
        below_row_idx = deepcopy(rook_row_idx)
        while below_row_idx < len(board)-1 and rook_col[below_row_idx] in ['.', 'R']:
            below_row_idx += 1            
        if rook_col[below_row_idx] == 'p':
            captures += 1
            
        left_col_idx = deepcopy(rook_col_idx)
        while left_col_idx > 0 and rook_row[left_col_idx] in ['.', 'R']:
            left_col_idx -= 1           
        if rook_row[left_col_idx] == 'p':
            captures += 1
            
        right_col_idx = deepcopy(rook_col_idx)
        while right_col_idx < len(board)-1 and rook_row[right_col_idx] in ['.', 'R']:
            right_col_idx += 1
        if rook_row[right_col_idx] == 'p':
            captures += 1
            
        return captures