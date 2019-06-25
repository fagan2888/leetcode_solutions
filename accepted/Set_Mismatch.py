## https://leetcode.com/problems/set-mismatch/submissions/

## pretty standard solution of using a hash table (in this case, 
## the specifically-built for this Count) to keep track of the 
## number of items in nums, then using a set intersection to 
## find the missing one.  comes in at 86th for runtime, though
## only 5th percentile for memory (sorting solution would work 
## better in that sense)

from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ## two ways to do this
        ## 1) sort then iterate until I find both -- worst-case is NlogN + N
        ## 2) use a counter and set subtraction -- building the counter is O(N), 
        ##      then finding the max is another O(N), so that way wins
        count = Counter(nums)
        missing = list(set(range(1, len(nums)+1)) - set(count.keys()))[0]
        duplicated = count.most_common(1)[0][0]
        return [duplicated, missing]
        