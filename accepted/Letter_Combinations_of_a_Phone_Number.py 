## https://leetcode.com/problems/letter-combinations-of-a-phone-number/

## pretty straightforward solution here -- loop over the digits, and add 
## to each of my current outputs (initialized as an empty string if we have
## any digits) each of the characters corresponding to that digit.

## take advantage of a double list comprehension for speed though, as
## python does those very well, as evidenced by the fact that this comes
## in at 99.64th percentile!  some weirdness in that though, as running 
## it again comes in at only 87th percentile...

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []
        
        digit_to_chars = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        outputs = ['']
        for d in digits:
            new_out = [o+c for c in digit_to_chars[d] for o in outputs]
            outputs = new_out
        return outputs