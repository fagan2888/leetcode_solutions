## https://leetcode.com/problems/excel-sheet-column-number/

## problem is to convert a column title in an excel spreadsheet
## into the number of that column (i.e. A -> 1, B -> 2, AA -> 27, ...)

## slightly trickier problem then I thought on first glance.  this 
## solution comes in at 68th percentile in runtime and 83rd percentile
## in memory

class Solution:
    def titleToNumber(self, s: str) -> int:
        import string
        
        ## what does each single digit translate to?
        single_digit_converter = dict(zip(string.ascii_uppercase[:26], range(1, 27)))        
        output = 0
        
        ### so, trying to think about this as a 
        ### combinatorics problem
        ### for final entry, just add val
        ### for second to last entry (one left), add val*26
        ### third to last (2 left), add (val)*26^2, and so on
        for ii, char in enumerate(s):
            n_after = len(s[ii+1:])
            val = single_digit_converter[char]
            if n_after == 0:
                output += val
            else:
                output += (val)*(26**n_after)
            
        return output