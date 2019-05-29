## https://leetcode.com/problems/substring-with-concatenation-of-all-words/submissions/

## this method fails on test case 171 of 173 because it's too slow.
## i'm not sure I see a way to avoid checking every starting position
## in s, and I'm also not sure I see a way to avoid having a loop over
## the words too.

## unfortunately, that means my complexity is O(len(s)*len(words)), which
## is too slow for a case where we have a ton of short words and a very long
## string.


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not len(words):
            return []
        if not len(s):
            return []
        
        from copy import copy
        
        output = []
        
        single_word_length = len(words[0])
        words_to_match = len(words)

        word_count = {}
        for w in words:
            word_count[w] = word_count.get(w, 0) + 1
        
        for ii in range(len(s)):
            mywords = copy(word_count)
            words_left = copy(words_to_match)
            index = copy(ii)
            
            while words_left > 0 and index < len(s):
                w = s[index:index+single_word_length]
                if mywords.get(w, 0) > 0:
                    mywords[w] = mywords[w] - 1
                    words_left = words_left - 1
                    index = index + single_word_length
                else:
                    break

            if words_left == 0:
                output.append(ii)
        
        return output