## https://leetcode.com/problems/string-to-integer-atoi/

## problem is to turn a string of numbers into an integer,
## without using the int function of course.  also have a bit
## more leeway in what's passed in -- we ignore whitespace, and
## stop parsing once we hit an invalid character.

## this solution is O(3*n) at worst case (where n is the length
## of our string) -- one loop to validate the characters, another
## to sum them up, and a third to create our multipliers.  
## fortunately, the loops are each trivial, so not really a 
## cause for concern (plus, still linear time)

## note that I hard-code the limits since python defaults to 64-bit
## integers, so we don't overflow like we should.

## comes out to ~58th percentile in runtime and 61st percentile in
## terms of memory

class Solution:
    def myAtoi(self, string: str) -> int:
        string = string.strip()

        ## strings that are empty (or only whitespace) 
        ## are invalid and return zero
        if not len(string):
            return 0
        
        minval = -2147483648
        maxval = 2147483647
        

        num_dict = {str(ii):ii for ii in range(10)}
        valid_chars = list(num_dict.keys())
        
        ## check that our first character (after stripping) is either
        ## a number or a plus/minus sign
        if string[0] not in valid_chars and string[0] not in ['-', '+']:
            return 0
        

        ## handle that first character if necessary
        if string[0] == '-':
            negative = True
            string = string[1:]
        else:
            if string[0] == '+':
                string = string[1:]
            negative = False
        

        ## loop over our string, appending the actual numbers
        ## using a lookup table for individual digits
        out_vals = []
        for ii, char in enumerate(string):
            if char not in valid_chars:
                break
            
            out_vals.append(num_dict[char])
        

        ## reverse that, multiply each by 10^n, where n is it's place in 
        num_digits = len(out_vals)
        rev_out = out_vals[::-1]
        multipliers = [10**n for n in range(num_digits)]
        rev_out_mult = [ov * m for ov, m in zip(rev_out, multipliers)]

        out = sum(rev_out_mult)
        if negative:
            out *= -1
            if out < minval:
                return minval
            return out
        else:
            if out > maxval:
                return maxval
            return out
        