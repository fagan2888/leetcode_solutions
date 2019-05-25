## https://leetcode.com/problems/number-complement/

## problem is to find the binary complement of a number
## i.e., turn all the 1s to 0s and 0s to ones.  there's
## definitely a much faster way to solve this problem,
## i.e. with fewer loops over the string, but the simple
## brute-force solution is fast enough -- turn it into a 
## binary string, replace all the 1s with 2s, then replace
## all the 0s with 1s, then all the 2s with 0s.

## comes in at only 11th percentile in runtime, though
## 84th percentile in memory (since we don't use any 
## extra structures; all is done in place)

class Solution:
    def findComplement(self, num: int) -> int:
        as_binary = f'{num:b}'
        as_binary = as_binary.replace('1', '2')
        as_binary = as_binary.replace('0', '1')
        as_binary = as_binary.replace('2', '0')
        return int(as_binary, 2)