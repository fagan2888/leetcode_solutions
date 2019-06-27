## problem is, given an area, find the length and width of a rectangle 
## that has that area that's closest to a square as possible.  that means
## finding all factor pairs of area, then returning the one with the 
## smallest difference between the two numbers.

## at first I used this solution, which gathers all the factors then 
## sorts them by the difference between them and returns the one with 
## the smallest difference.  that come in at 40ms, for a runtime of 
## 53rd percentile and memory of 69th percentile.
# from math import sqrt, ceil
# class Solution:
#     def get_factors(self, num: int) -> List[List[int]]:
#         factors = []

#         ## only have to loop up to sqrt(num) since we get both 
#         ## factors each time we find one
#         for ii in range(1, ceil(sqrt(num))+1):
#             if num % ii == 0:
#                 factors.append([num//ii, ii])
#         return factors
        
    
#     def constructRectangle(self, area: int) -> List[int]:
#         factors = sorted(self.get_factors(area), key=lambda x: abs(x[0]-x[1]))        
#         return factors[0]


## but then I realize that was stupid -- because I'm looking for the smallest 
### difference, I should just loop from sqrt(x) down until I find a factor, and
## then that factor is required to have the smallest difference (otherwise I 
## would have hit a better one before it.  that meaqns less looping, which gets
## me down to 32ms, good enough for ~98.6 percentile for runtime and 79.6 percentile 
## for memory.  here's that (better) solution:

from math import sqrt, ceil
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for ii in reversed(range(1, ceil(sqrt(area))+1)):
            if area % ii == 0:
                return sorted([area//ii, ii])[::-1]