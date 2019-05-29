## https://leetcode.com/problems/roman-to-integer/

## problem is to convert a string of roman numerals
## into a base ten integer.  do it on O(n) time -- 
## at each spot, check if the next character (if there
## is one) is larger, and if so, we subtract this character.

## otherwise, we simply add it up!

## comes in at 99.6th percentile in runtime and 66th 
## percentile in memory

class Solution:
    def romanToInt(self, s: str) -> int:
        translator = {'I':1,
                      'V':5,
                      'X':10,
                      'L':50,
                      'C':100,
                      'D':500,
                      'M':1000}
        
        output = 0
        for ii, char in enumerate(s):
            if ii == len(s) - 1:
                output = output + translator[char]
            elif translator[s[ii+1]] > translator[char]:
                output = output - translator[char]
            else:
                output = output + translator[char]
        return output