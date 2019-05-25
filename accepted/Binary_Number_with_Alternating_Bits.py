## https://leetcode.com/problems/binary-number-with-alternating-bits/

## problem is to check whether a given number is composed of 
## purely alternating bits when expressed in binary form (i.e. 
## ...1010101...).  there's probably a faster way to do this via
## a list comprehension (i.e. something like:
## if False in [num_as_bin[ii] != num_as_bin[ii+1] for ii in range(len(num_as_bin)-1)]),
## but even this simple looping solution (O(len(num_as_bin)) in worst
## case scenario, though I'm not positive of the complexity of
## expressing a number in binary, comes in at 91st in terms of 
## runtime and 70th in memory

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        num_as_bin = f'{n:b}'
        
        idx = 0
        last_num = num_as_bin[idx]
        for index in range(1, len(num_as_bin)):
            if last_num == num_as_bin[index]:
                return False
            
            last_num = num_as_bin[index]
        return True