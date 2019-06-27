## https://leetcode.com/problems/reverse-words-in-a-string-iii

## this one is actually easier than II because we just split on 
## empty space, then join the reversed words around a space

## comes in at ~91st percentile for runtime and 91st for memory.

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(w[::-1] for w in s.split())