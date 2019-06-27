## https://leetcode.com/problems/verifying-an-alien-dictionary

## a little surprised this scores so highly, since it's a roughly 
## O(N*M)), where M is the number of characters in each string, but
## comes in at ~85th percentile for runtime and 27th for memory.

## solution is to turn the order into a lookup table, then iterate
## over each pair of words until I find a differint letter.  once 
## i do, return false if those letters are in the word order.

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        indices = {char: ii for ii, char in enumerate(order)}
        
        for word, next_word in zip(words[:-1], words[1:]):
            ## find first different character:
            idx = 0
            while idx < min(len(word), len(next_word)):
                if word[idx] != next_word[idx]:
                    break
                idx += 1
            
            if idx == len(word):
                ## hit the end of (at least) the first word, which means it should come first
                pass
            
            elif idx == len(next_word):
                ## hit the end of the second word but not the first
                ## which means second should be first, so return False
                return False
            
            else:
                ## didn't hit the end of either word -- check if first differing character 
                ## is sorted correctly:
                if indices[word[idx]] > indices[next_word[idx]]:
                    return False
        return True