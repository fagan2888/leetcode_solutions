## https://leetcode.com/problems/find-all-duplicates-in-an-array/

## pretty simple solution -- use a set to keep track of the numbers
## that have already appeared (because lookup time is O(1) given 
## the implementation in python via a hash table).  Gives me an O(N)
## runtime

## runetime is 79th percentile; memory is 19th percentile

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        already_appeared = set([])
        twice = []
        
        while len(nums):
            n = nums.pop()
            
            if n in already_appeared:
                twice.append(n)
            else:
                already_appeared.add(n)
        return twice
        
        