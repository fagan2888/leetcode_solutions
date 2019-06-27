## https://leetcode.com/problems/guess-number-higher-or-lower

## this question is really weirdly defined.  basically I'm just looking 
## for an unknown number given a range it's in (1 - n).  that means I'm 
## doing a search for a number in a sorted list basically, so just do a 
## simple logarithmic search.

## comes in at 95th percentile for runtime and 78th for memory

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        mid = (left+right)//2
        
        res = guess(mid)
        while res != 0:
            if res < 0:
                ## my guess is too high, so set right to mid
                right = mid
                mid = (left+right)//2
            else:
                left = mid
                mid = (left+right)//2 + 1
            res = guess(mid)
        
        return mid