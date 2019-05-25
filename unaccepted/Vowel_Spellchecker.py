## https://leetcode.com/problems/vowel-spellchecker/

## problem is to spellcheck queries against a valid wordlist.
## spellcheck/possible corrections are defined as subbing all 
## vowels in the word with all other (i.e., only the vowels 
## can be wrong).

## unsurprisingly, this dumb, brute-force solution is too slow
## because every vowel we hit increases our possible word list 
## by five.  

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        from copy import copy
        output = []
        
        vowels = 'aeiou'
        
        lower_words = [w.lower() for w in wordlist]
        
        for query in queries:
            ## first check for any matches in the valid wordlist
            if query in wordlist:
                output.append(query)
                continue
            
            ## and do the same for lower-case
            q = query.lower()
            if q in lower_words:
                output.append(wordlist[lower_words.index(q)])
                continue
                

            ## build up the list of possible words we can make 
            ## out of the consonants in our word + all possible vowels
            possible_words = ['']

            ## loop over the characters
            for c in q:
                ## if it's not a vowel, we just add this character to every
                ## word in our list
                if c not in vowels:
                    new_words = [w+c for w in possible_words]
                    possible_words = new_words

                ## if it is a vowel, we have to add 5 new possible paths to our
                ## words -- ___+a, ___+e, ___+i, ....
                else:
                    new_words = [oldr + v for v in vowels for oldr in possible_words]
                    possible_words = new_words

            ## now we loop over those possible words and 
            ## check if any of them are in the wordlist.

            ## if they are, we return the first entry to 
            ## appear in the wordlist
            found_words_by_index = {}
            for w in possible_words:
                if w in lower_words:
                    idx = lower_words.index(w)
                    found_words_by_index[idx] = wordlist[idx]

            ## https://leetcode.com/problems/vowel-spellchecker/

            ## problem is to spellcheck queries against a valid wordlist.

        ## spellcheck/possible corrections are defined as subbing all 
        ## vowels in the word with all other (i.e., )


            ## if there aren't any, we return an empty string
            if len(found_words_by_index) == 0:
                output.append('')
            else:
                output.append(found_words_by_index[min(found_words_by_index.keys())])
        return output
                    
             