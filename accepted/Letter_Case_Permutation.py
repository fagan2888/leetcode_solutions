## https://leetcode.com/problems/letter-case-permutation/

## this one is pretty straightforward if you know what you're doing with
## itertools.  that said, there is clearly a more optimal solution (I'm 
## brute forcing here) -- either my way of building the indices is suboptimal
## or the way I'm building each output string could be better.  this comes in 
## at only 8th percentile for runtime, though it does feature 46th percentile
## for memory.

import itertools
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        letter_indices = [ii for ii in range(len(S)) if S[ii] not in set('1234567890')]
        
        S_all_lower = S.lower()
        
        out = [str(S_all_lower)]
        for upper_indices in itertools.chain.from_iterable([itertools.combinations(letter_indices, n) for n in range(1, len(letter_indices)+1)]):
            so = ''.join([S_all_lower[ii].upper() if ii in set(upper_indices) else S_all_lower[ii] for ii in range(len(S))])
            out.append(so)
        return out