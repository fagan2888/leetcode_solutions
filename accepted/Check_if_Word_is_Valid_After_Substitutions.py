## https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

## not quite a one-liner, but close!  basically, we can 
## keep removing abc from a string, and if are able to 
## remove the entire string, then we had a valid string.
## so, do it brute force, but it's quick!  comes in at
## 99th percentile for runtime and 82nd for memory.

class Solution:
    def isValid(self, S: str) -> bool:
        while 'abc' in S:
            S = S.replace('abc', '')
        return len(S) == 0