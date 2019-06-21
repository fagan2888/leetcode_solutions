## https://leetcode.com/problems/integer-to-roman/submissions/

## simple, though not the fastest, solution -- just decrement our 
## number by the largest value we can (where we've preprogrammed
## the values we can decrement by, including IV, IX, etc.).  comes
## in at 23rd for runtime and 66th for memory.

class Solution:
    def intToRoman(self, num: int) -> str:
        indiv_converters = {1   : 'I',
                            5   : 'V',
                            10  : 'X',
                            50  : 'L',
                            100 : 'C',
                            500 : 'D',
                            1000: 'M', 
                            4 : 'IV',
                            9:  'IX',
                            40 : 'XL', 
                            90 : 'XC',
                            400 : 'CD',
                            900 : 'CM'}
        
        out = ''
        while num > 0:
            max_can_sub = max(v for v in indiv_converters if v <= num)         
            out = out + indiv_converters[max_can_sub]
            num = num - max_can_sub
        return out