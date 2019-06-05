## https://leetcode.com/problems/lexicographical-numbers/

## probably wouldn't bother putting this one up here because it's
## so short, but apparently this method is about as fast as you can
## get -- use the built in sorted + range, and tell sorted that our
## comparison key is the string-ed value

## comes in at 99th percentile for runtime and 38% percentile for 
## memory.  the lesson -- use built in python libraries whenever possible

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(range(1, n+1), key=str)