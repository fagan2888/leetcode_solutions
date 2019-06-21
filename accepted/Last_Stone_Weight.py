## https://leetcode.com/problems/last-stone-weight

## pretty simple solution -- sort the list, so I can pop off the last two items 
## each time, then use bisect.insort to insert into the sorted list.  that insort
## still takes O(n) because inserting into a list is expensive...can I speed it
## up?  

## turns out that the fastest time I get (~99th percentile) is the below -- using 
## bisect.bisect then inserting myself by concatenating lists is slower.  both solutions
## come out to 100th percentile for memory though, since it's O(1)

from bisect import insort

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        while len(stones) > 1:
            s1 = stones.pop()
            s2 = stones.pop()
            
            if s1 != s2:
                insort(stones, abs(s1-s2))

        if not len(stones):
            return 0
        return stones[0]