## https://leetcode.com/problems/integer-to-english-words/

## this is a hard one, and it was hard because it's super 
## annoying and has a ton of edge cases.  my solution is 
## reasonably fast -- not many 'in' checks and mostly just
## direct comparisons and lookup tables.  again, tons of 
## edge cases to catch though.

## anyway, start at the end of the number (i.e. 000 -- 999), 
## zero to nine hundred nintey-nine.  handle it as a group,
## but figure out whehter or not we put "hundred", whether or 
## not we have teens, etc., then basically repeat for higher
## groups of three.

## comes in at 33rd percentile for runtime and 54th for memory.
## i'll take it, just to be done with this problem.

from functools import lru_cache

class Solution:
    def numberToWords(self, num: int) -> str:
        values = {0: 'Hundred',
                  1: 'Thousand',
                  2: 'Million',
                  3: 'Billion',
                  4: 'Trillion',
                  5: 'Quadrillion',
                  6: 'Quintillion',
                  7: 'Sextillion', 
                  8: 'Septillion', 
                  9: 'Octillion'}
        
        ones_converter = {'1': 'One', '2':'Two', '3':'Three', '4':'Four',
                         '5':'Five', '6':'Six', '7':'Seven', '8':'Eight',
                         '9':'Nine', '0': 'Zero'}
        
        teens_converter = {'11': 'Eleven', '12':'Twelve', '13':'Thirteen',
                           '14':'Fourteen', '15':'Fifteen', '16':'Sixteen',
                           '17':'Seventeen', '18':'Eighteen','19':'Nineteen', 
                          '10':'Ten'}
        
        tens_converter = {'2':'Twenty', '3':'Thirty', '4':'Forty', '5':'Fifty',
                         '6':'Sixty', '7':'Seventy', '8':'Eighty', '9': 'Ninety'}
        
        @lru_cache(None)
        def convert_1_to_9(snum):
            return ones_converter[snum]
        
        @lru_cache(None)
        def convert_1_to_99(snum):
            n = int(snum)
            assert n < 100
            if n < 10:
                if len(snum) == 1:
                    return ones_converter[str(snum)]
                else:
                    ## have a 0X, i.e. 101 => 01 for this function
                    return ones_converter[str(snum)[-1]]
            if n < 20:
                return teens_converter[str(snum)]
            else:
                tens = tens_converter[snum[0]]
                if snum[1] == '0':
                    ones = ''
                else:
                    ones = ' ' + ones_converter[snum[1]]
                return tens + ones                
        
        def convert_zero_to_999(snum):
            if len(snum) == 1:
                return convert_1_to_9(snum)
            elif len(snum) == 2:
                return convert_1_to_99(snum)
            else:
                if snum[0] == '0':
                    hundreds_string = ''
                else:
                    hundreds_string = convert_1_to_9(snum[0]) + ' Hundred'
                if snum[1:] == '00':
                    tens_down = ''
                else:
                    tens_down = convert_1_to_99(snum[1:])
                return hundreds_string + ' ' + tens_down    
        
        ## partition into groups of 3, starting at the end
        rsnum = str(num)[::-1]
        pval = [rsnum[3*ii:3*ii+3][::-1] for ii in range(len(rsnum)//3)]
        included_chars = sum(len(s) for s in pval)
        leftovers = rsnum[included_chars:]
        pval = pval + [leftovers[::-1]]
        
        output_strings = []
        for ii, group in enumerate(pval):
            if len(group) == 0:
                continue
            
            v = values[ii]
            if len(group) == 2:
                out = convert_1_to_99(group)
            elif len(group) == 1:
                out = convert_1_to_9(group)
            else:
                out = convert_zero_to_999(group)
            if ii != 0 and group != '000':
                out = out + ' ' + v
            
            output_strings.append(out.strip())
        
        out = ' '.join(output_strings[::-1]).strip().replace('  ', ' ')
        while '  ' in out:
            out = out.replace('  ', ' ')
        return out        