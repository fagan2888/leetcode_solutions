## https://leetcode.com/problems/valid-parentheses/

## check if a string is a valid set of parentheses.  
## classic problem to solve with a stack (last in last out),
## which in python is just implemented as a list

## so we do this in O(n), since we loop over the list 
## just once.  all operations are O(1) since they're 
## just equality checks and hash table lookups

## and indeed, we come in at the the 99.58th percentile, 
## though only 14th percentile in terms of memory

class Solution:
    def isValid(self, s: str) -> bool:
        open_characters = []
        
        matcher = { '(' : ')',
                    '{' : '}', 
                    '[' : ']'
                  }
        for char in s:
            if char in matcher:
                open_characters.append(char)
            else:
                if not len(open_characters):
                    return False
                if char != matcher[open_characters.pop()]:
                    return False
        
        if len(open_characters):
            return False
        else:
            return True