## https://leetcode.com/problems/detect-capital/

## given a single word that is just upper and lowercase letters,
## determine whether it uses capital letters correctly according
## to the three following rules:

# True if:
# All letters in this word are capitals, like "USA". or 
# All letters in this word are not capitals, like "leetcode". or 
# Only the first letter in this word is capital, like "Google".

## i'm not positive of the complexity of the operations .upper and 
## .lower, but I think python might optimize with the != and stop
## checking once it hits a disagreement -- another method that has
## a capitalize, an upper, and a lower, but all =='s, is consistently
## slower.  this comes in at 97-99th percentile for runtime and 47th
## percentile for memory.


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        ## does the word have lowercase letters?
        has_lowercase = (word.upper() != word)

        ## does the word have upercase letters?
        has_uppercase = (word.lower() != word)
        
        ## if it has uppercase letters, are they used corrected?
        if has_uppercase:
            ## all uppercase?  correct!
            if not has_lowercase:
                return True

            ## only first letter is uppercase?  correct!
            elif word[1:].lower() == word[1:]:
                return True

            ## anything else?  wrong
            else:
                return False

        ## no uppercase letters at all?  all good!
        else:
            return True