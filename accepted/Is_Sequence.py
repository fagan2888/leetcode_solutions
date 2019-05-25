## https://leetcode.com/problems/is-subsequence/

## asked to check if a given string s (which is very short) 
## is a substring/subsequence of t (i.e. can we delete characters
## from t, without reordering it, to get s).   t here is 
## potentially very long.

## this solution seems less than ideal, since our worst-case scenario
## runtime is O(len(s)*len(t)), since for each character in s we do a 
## search of t (which can be very long).  however, the search terminates
## once it finds a letter, so it can be very fast (since we only ask 
## for the first each tmie), and then we throw away all characters
## in t before the first instance of the letter we're looking for.
## therefore, if s occurs at the very end of a very long string
## t, then we'll only have to search that very long string once.
## likewise, if a character occurs at the beginning of t, then we 
## don't have to search very far into t.  worst-case runtime would
## be if the characters of s are equally spaced throughout a very
## long string.

## comes in at 91st percentile in runtime and 19th 
## percentile in memory

## add a method to str to find first index or -1 if character
## isn't in there
class myString(str):
    def my_index(self, char):
        if char in self:
            return self.index(char)
        else:
            return -1

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = myString(t)
        for char in s:
            idx = t.my_index(char)
            if idx < 0:
                ## if we ever fail to find the next character in s 
                ## in the remaining portion of t, then s is not a 
                ## subsequence of t
                return False
            else:
                t = myString(t[idx+1:])
        return True