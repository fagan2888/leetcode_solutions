## https://leetcode.com/problems/shortest-completing-word/

## worst case complexity is roughly O(len(words)*len(licensePlate))
## surprisingly, that still ends up in the 99th percentile for runtime
## and 35th perecentile for memory

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        from copy import copy
        
        ## pull out the letters from the license plate
        letters = ''.join([l for l in licensePlate.lower() if l in 'abcdefghijklmnopqrstuvwxyz'])
        
        ## put all of our words in lowercase for easy comparison
        lower_words = [w.lower() for w in words]
        
        ## sort the words by length so we return the shortest 
        sorted_words = sorted(lower_words, key = len)
        
        for w in sorted_words:
            is_complete_word = False

            ## make a copy because we're going to pop letters out of this word
            my_word = copy(w)

            ## iterate over the letters in the license plate and pop them out of 
            ## the current word if we find them.  if we don't find a letter, break,
            ## because that means this word is wrong.
            for ii, l in enumerate(letters):
                new_w = my_word.replace(l, '', 1)
                if len(new_w) == len(my_word):
                    ## letter l not in w cause we got the same thing out, so move on to next word
                    break
                else:
                    ## letter l is in w (though not anymore)
                    my_word = new_w
                    
                    ## if we've looped through all of our letters 
                    if ii == len(letters) - 1:
                        is_complete_word = True
 
            if is_complete_word:
                result = w
                break

        return result