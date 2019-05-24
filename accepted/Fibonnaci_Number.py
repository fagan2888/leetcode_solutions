## https://leetcode.com/problems/fibonacci-number/

## classic problem -- calculate a Fib number.  I'm implementing 
## this as a iterative problem with a memory, so complexity is O(N).

## ends up at 86th percentile in runtime but only 12th percentile in memory
## (unsurprisingly since we're keeping a memory of all lower fib numbers)

class Solution:
    def __init__(self):
        self.previous_N = {0:0, 1: 1, 2: 1, 3: 2}
        self.max_previous_N = 3
    
    def fib(self, N: int) -> int:
        if self.max_previous_N >= N:
            return self.previous_N[N]
        
        else:
            starting_val = self.max_previous_N + 1
            for ii in range(starting_val, N+1):
                self.previous_N[ii] = self.previous_N[ii-1] + self.previous_N[ii-2]
            return self.previous_N[N]