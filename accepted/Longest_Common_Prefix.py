## https://leetcode.com/problems/longest-common-prefix/

## Find the longest prefix in common between a list of words.

## my solution is to sort the words by length, so that I can 
## use the first to set the possible prefixes.  then, I iterate
## from the length of that word down to zero, and return True
## if I ever find that all the words in the list (except that
## first, which is gauranteed to be true) start with that 
## string.  if we get to the end, return an empty string

## comes in at 98th percentile for runtime and ~22nd 
## percentile for memory

class Solution:
    def longestCommonPrefix(self, words: List[str]) -> str:
        if not len(words):
            return ''
                
        ## sort from shortest to longest
        words = sorted(words, key=len)
        
        if not len(words[0]):
            return ''

        for ii in reversed(range(len(words[0]))):
            base = words[0][:ii+1]
            
            if False not in [w.startswith(base) for w in words[1:]]:
                return base
        return ''