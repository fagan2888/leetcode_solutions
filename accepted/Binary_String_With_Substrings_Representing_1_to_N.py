## https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

## another relatively simple medium I think -- the brute-force solution 
## is not only accepted, it comes in at 94th percentile for runtime and 
## 23rd for memory.

## in principle, I'd have guessed that a smarter solution where we 
## incrememnt a binary number would be quicker, but I guess not that
## much faster (if faster at all.)

class Solution:
    def int_to_bin(self, n: int) -> str:
        return f'{n:b}'
    
    def queryString(self, S: str, N: int) -> bool:
        for n in range(1, N+1):
            if self.int_to_bin(n) not in S:
                return False
        return True