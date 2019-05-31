## https://leetcode.com/problems/battleships-in-a-board/

## goal is to count the number of battleships in a board, 
## under the condition that no battleships will ever touch.

## that means that any touching x's belong to the same 
## battleship.  my solution is to iterate over the board, 
## so O(N).  If i find a part of a ship, I check the spots
## above and to the left for another part of a ship.  If I
## find one, then I move on; if I don't, then I add to my 
## ship count.

## comes in at 51st percentile for runtime and 13th percentile
## for memory.


class Solution:
    def valid_neighbors(self, row_index: int, col_index: int) -> List[int]:
        return filter(lambda pair:  pair[0] >= 0 and pair[1] >= 0, 
                     [[row_index-1, col_index], [row_index, col_index-1]])
    
    def countBattleships(self, board: List[List[str]]) -> int:
        nships = 0
        for row_index, row in enumerate(board):
            for col_index, val in enumerate(row):
                if val == 'X':
                    is_part_of_prev_ship = False
                    earlier_neighbors = self.valid_neighbors(row_index, col_index)
                    for coord in earlier_neighbors:
                        if board[coord[0]][coord[1]] == 'X':
                            is_part_of_prev_ship = True
                            break
                    if not is_part_of_prev_ship:
                        nships = nships + 1

        return nships
