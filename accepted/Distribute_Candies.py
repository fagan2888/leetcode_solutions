## https://leetcode.com/problems/distribute-candies/

## given an even number of candies (i.e. an even lengthed array
## with different numbers that represent different candies), 
## figure out how many KINDS of candy the sister can get, 
## assuming that the total candies have to be distributed 
## equally.

## solve this by finding out how many unique candies we have,
## then returning either the number of unique candies (if it's
## less than half the total divided by two; i.e. if the sister
## can't get entirely unique candies) or half the candies

## runtime is therefore O(N) to build the set, and everything 
## else is pretty trivial

## comes in at 84th percentile in runtime and 32nd in memory

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        unique_candy_types = set(candies)
        tot_candies = len(candies)
        tot_unq_candies = len(unique_candy_types)
        if tot_unq_candies < tot_candies/2:
            return tot_unq_candies
        
        return int(tot_candies / 2)