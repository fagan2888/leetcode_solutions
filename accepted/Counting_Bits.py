## https://leetcode.com/problems/counting-bits/

## for every number between 0 and N, count up the 
## number of 1-bits in that number.  I briefly tried
## writing this up more intelligently by iterating 
## a number in binary up to N, but it wasn't quite
## working and it turns out the simple way (using
## built in base conversion) is fast enoguh (25th
## percentile in runtime and 64rd in memory).

class Solution:
    def add_one_to_binary(self, num):
        return f'{int(num, 2) + 1:b}'
            
    
    def countBits(self, num: int) -> List[int]:
        number = '0'
        output = [0]
        for ii in range(1, num+1):
            number = self.add_one_to_binary(number)
            output.append(number.count('1'))
        return output