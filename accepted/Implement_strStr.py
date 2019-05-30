## https://leetcode.com/problems/implement-strstr/

## problem is to find where the needle occurs in the haystack.

## do this in O(n) by looping over the characters in the haystack
## and checking if the string started by that index (and as long
## as the needle) is equal to the needle.

## return -1 if we get to the end cause it's not in there.

## comes in at 99.46th percentile for runtime, but only 10th
## for memory

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nlen = len(needle)
        if not nlen:
            return 0
        
        if not len(haystack):
            return -1
        
        for ii in range(len(haystack)-nlen+1):
            if haystack[ii:ii+nlen] == needle:
                return ii
            
        return -1