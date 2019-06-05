## https://leetcode.com/problems/valid-boomerang/

# problem:  check if three points are NOT in a line
# solution:  fit a line to the first two, check if third
# lines up with where it says it should be, and return 
# false if it does.  and then there are edge cases.

# runtime is 98th percentile.  somehow memory usage is
# 100th percentile, which is shocking since I'm not being
# careful about that at all -- what are people doing?


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        xs = [p[0] for p in points]
        ys = [p[1] for p in points]
        
        ## edge cases:  two points are identical
        if (xs[0] == xs[1] and ys[0] == ys[1]) or (xs[1] == xs[2] and ys[1] == ys[2]) or (xs[0] == xs[2] and ys[0] == ys[2]):
            return False
        
        ## vertical line between x0 and x1 (i.e. can't get slope from them)
        if xs[0] == xs[1]:
            return xs[0] != xs[2]
        
        ## otherwise, fit from the first two 
        ## point and compare prediction with 
        ## the third
        m = (ys[1] - ys[0])/(xs[1] - xs[0])
        
        
        ## y = m x + b => b = y - m*x
        b = ys[0]  - (m*xs[0])
        
        ## now compare:
        return m*xs[2] + b != ys[2]
        