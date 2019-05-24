## https://leetcode.com/problems/permutations/

## this one is almost cheating...itertools is available
## and it can do permutations automatically.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        return list(permutations(nums))