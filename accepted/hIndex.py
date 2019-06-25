## https://leetcode.com/problems/h-index/

## calculate an h-index given a list of citation counts.
## solution -- sort them, then iterate until you hit a 
## paper with fewer than it's 1-based index citations.
## your h-index is then that one.

## got 100th percentile for runtime and 42nd for memory!

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)[::-1]
        idx = 0
        N = len(citations)
        while idx < N:
            if citations[idx] < idx+1:
                break
            idx += 1
        return idx