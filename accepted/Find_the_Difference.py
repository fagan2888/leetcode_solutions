## https://leetcode.com/problems/find-the-difference/

## brute force method -- sort the strings, then break when 
## the two don't match up (much faster if we had access
## to numpy arrays).  O(log(N)) to sort the strings, then
## a worst-case O(N) for the comparison loop 

## of course, this is relatively slow (since it's brute
## force), so we only come in at 12th percentile in terms
## of runtime and 28th in terms of memory

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        
        for ii in range(len(t)):
            if ii == len(s):
                return t[ii]  #then it's the last one 
            if t[ii] != s[ii]:
                return t[ii]
