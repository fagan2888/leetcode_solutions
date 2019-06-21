## https://leetcode.com/problems/string-compression/

## this one isn't too tough; we can do it in effectively one pass here.
## it again just relies on keeping track of the number of times that
## we've seen the same character in a row, then doing something when we
## find a new one.  in this case, that something is replacing the 2nd through
## (N+1)th occurence with the digits of the number of times that char appears,
## then deleting the rest.  means that you have to update some indices of 
## course, and we only do the compression if we have more than 1 character
## (otherwise, nothing to compress).

## comes in at 72nd percentile for runtime and 48th for memory.

class Solution:
    def compress(self, chars: List[str]) -> int:
        if not len(chars):
            return []
        
        count = 1
        schar = chars[0]
        sidx = 0
        
        index = 1
        while index < len(chars):
            c = chars[index]
            if c == schar:
                count = count + 1
                index = index + 1
                continue
            else:
                ## decide whether or not to compress this string.
                ## basically comes down to whether or not we have 
                ## more than 2
                if count >= 2:
                    count = str(count)
                    ii = sidx + 1
                    for d in count:
                        chars[ii] = d
                        ii = ii + 1
                        
                    ## now delete the remaining entries of that character
                    while ii < len(chars) and chars[ii] == schar:
                        del chars[ii]
                        ## and shift back my current index accordingly
                        index = index - 1
                
                ## now I've compressed (or not) the previous char; start a new one
                schar = str(c)
                count = 1
                sidx = int(index)
                
                index = index + 1
        
        ## and now compress the final run:
        if count >= 2:
            count = str(count)
            ii = sidx + 1
            for d in count:
                chars[ii] = d
                ii = ii + 1

            ## now delete the remaining entries of that character
            while ii < len(chars) and chars[ii] == schar:
                del chars[ii]
                ## and shift back my current index accordingly
                index = index - 1              
                    
                    