## https://leetcode.com/problems/jewels-and-stones/

## given a list of jewels J and a list of stones S, return
## the number of stones we have that are jewels.  

## do this via a list comprehension with a filter,
## which is very fast in python.  comes in at 92nd
## percentile in runtime and 70th in memory

## note that this solution is python2, since this problem
## didn't have a python3 option

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return len([s for s in S if s in J])
