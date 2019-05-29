## https://leetcode.com/problems/valid-number/

## determine whether a given string can be parsed to 
## a valid number (but don't actually parse it).  

## this is sort of a brute-force way, but it really
## comes down to keeping track of what we've passed
## as we iterate over the string (split by any exponent)
## and making sure we don't introduce any invalid characters.

## if we do, we return False, but if we get to the end of 
## the string and all the checks, we return True.

## roughly O(n) runtime, since we only touch each element 
## once.  however, there are several .counts at the beginning,
## which require an internal iteration over the string, along
## with a .split, which also requires iteration until we find
## the character (or over the whole string if we don't find it).
## that means our runtime is some constant time O(n), so still
## linear time (not bad).

## indeed, this makes it into the 90th percentile for runtime
## and the 69th percentile for memory (brought down by the 
## digits set at the beginning)

class Solution:
    def isNumber(self, s: str) -> bool:
        digits = set([str(x) for x in range(10)])
        
        ## remove any white space:
        s = s.strip()
        
        import string      

        ## make sure we have no more than one decimal point
        dec_count = s.count('.')
        if dec_count > 1:
            return False
        
        ## make sure we have no more than one e:
        e_count = s.count('e')
        if e_count > 1:
            return False
        
        ## make sure we have no more than two +/- 
        ## (one for the num, one for the exponent)
        plus_count = s.count('+')
        minus_count = s.count('-')
        if plus_count > 2 or minus_count > 2:
            return False
        
        ## make sure we have some digits leftover
        if plus_count + minus_count + e_count + dec_count == len(s):
            return False
        
        if 'e' in s:
            before_e, after_e = s.split('e')
            if not len(after_e):
                return False
            
            ## need at least one digit following the decimal point to 
            ## be a valid number
            if True not in [c in digits for c in after_e]:
                return False
        else:
            before_e = s
            after_e = ''
            
        ## need some digits before the exponent to be a valid
        ## number
        if True not in [c in digits for c in before_e]:
            return False
        
        after_dot = False
        for ii, char in enumerate(before_e):
            if char in string.ascii_letters:
                ## only e is allowed as far as letters go, 
                ## and we already split on it (so it's gone)
                return False
            
            if char in ['+', '-'] and ii != 0:
                ## +/- are only allowed at the start
                return False
            
            if char == '.':
                if after_dot:
                    ## can't have two decimal points before the exponent
                    return False
                after_dot = True
                continue
                
            if char == ' ':
                ## can't have spaces within the number
                return False
                
            if after_dot:
                ## only digits are allowed to follow the decimal point
                if char not in digits:
                    return False
                
                
        for ii, char in enumerate(after_e):
            ## only allowed to have +/- exponents immediately after the e
            if char in ['+', '-'] and ii != 0:
                return False
            
            ## no decimal points allowed after the exponent
            if char == '.':
                return False
            
            if char == ' ':
                ## can't have spaces within the exponent either
                return False            

            if char in string.ascii_letters:
                ## only e is allowed as far as letters go, 
                ## and we already split on it (so it's gone)
                return False
            
            
        return True