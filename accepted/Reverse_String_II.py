## https://leetcode.com/problems/reverse-string-ii

## goal is to reverse every other k-sized chunk of the
## string.  do this by chunking the list, then flipping
## every other, then joining.  comes in at 99th percentile
## for speed and 84th for memory.

class Solution:
    def chunk_iterable(self, input_iter: List, chunk_size: int) -> List:
        for ii in range(0, len(input_iter), chunk_size):
            yield input_iter[ii:ii + chunk_size]
    
    def reverseStr(self, s: str, k: int) -> str:
        chunked = list(self.chunk_iterable(s, k))
        for ii in range(len(chunked)):
            if ii % 2 == 0:
                chunked[ii] = chunked[ii][::-1]
        return ''.join(chunked)