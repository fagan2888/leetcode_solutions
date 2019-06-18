## https://leetcode.com/problems/k-closest-points-to-origin/

## not sure why this qualifies as a medium problem; it's pretty easy.
## just sort the points by their dist^2 (for speed), then return the 
## first K.

## comes in at 93rd percentile for speed and 87th for memory though

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist2 = lambda x:  x[0]**2 + x[1]**2
        points = sorted(points, key=dist2)
        return points[:K]
        
        