## https://leetcode.com/problems/count-and-say/

## this problem seems hard at first, but that's mostly
## because it's incredibly poorly described.  went to 
## wikipedia and it makes sense.  for ease, I went ahead
## and hard-coded in the first 5; after that, we generate 
## from the previous one.

## generating the next one is actually pretty easy -- just 
## loop over the string and keep track of how many times
## you hit the same number in a row, then when you hit a new
## number, update the output string with the number of times 
## you saw the previous number (then make sure to catch the
## final run outside the loop).

## runtime comes in at ~94th percentile and memory comes in 
## at ~86th percentile.

class Solution:
    def generate_next(self, seq: str) -> str:
        char = seq[0]
        count = 1
        out = ''
        for c in seq[1:]:
            if c == char:
                count = count + 1
            else:
                out = out + str(count) + char
                char = c
                count = 1
        ## now the final string of numbers:
        out = out + str(count) + char
        return out
    
    def countAndSay(self, n: int) -> str:
        ## ok so the description of the problem is terrible.  from wikipedia:
        
        ## To generate a member of the sequence from the previous member, 
        ## read off the digits of the previous member, counting the number 
        ## of digits in groups of the same digit.
        
        ## so, 1st term is "one one", so the second term is "11".
        ## second term is then "two ones", so the third term is "21"
        ## then you read one 2, one 1s => 1211, etc.
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        if n == 3:
            return '21'
        if n == 4:
            return '1211'
        if n == 5:
            return '111221'
        
        myn = 5
        seq = '111221'
        
        while myn < n:
            myn += 1
            seq = self.generate_next(seq)
            
        return seq