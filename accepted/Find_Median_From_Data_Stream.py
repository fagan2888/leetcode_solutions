## https://leetcode.com/problems/find-median-from-data-stream

## this one is classified as hard, but a relatively simple (but well 
## thought-out solution) works (albeit slowly compared to the rest of)
## the solutions.  I think it could be sped up if I thought a bit more
## carefully about how I handle the left and right -- I dobut that I
## actually need to the insort, and I could probably instead get away 
## with a simple comparison to the first/left entry of the right/left
## lists.

## anyway, this solution is O(n) to add a number, but O(0) to find the 
## median.  comes in at 6th percentile for runtime, though somehow 
## 89th percentile for memory.

# from collections import Counter, deque
from bisect import insort
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.median = None
        self.left = []
        self.right = []
        self.nitems = 0

    def addNum(self, num: int) -> None:
        if self.nitems == 0:
            self.median = num
        elif self.nitems % 2 == 1:
            ## had an odd lengthed stream, where median was one of the items.  now moving to 
            ## an even lengthed stream, so have to shift median to left or right and add num 
            ## to the other, then set median to be the halfway point between left[-1] and right[0]
            if num >= self.median:
                # >= because if equal we just add the same number to both and it doesn't matter
                
                ## we don't know where num goes in right, so insort it
                insort(self.right, num)
                
                ## we do know that median goes at the end of left, since it's 
                ## by definition larger than all other numbers in that list
                self.left.append(self.median)
            else:
                ## do the opposite of above:
                ## don't know where num goes in left:
                insort(self.left, num)
                
                ## median goes at the start of self.right
                self.right = [self.median] + self.right
                
            ## now set our new median -- guaranteed to have a number in both lists
            self.median = 0.5*(self.left[-1] + self.right[0])
        else:
            ## did have an even length stream (so median was a middle val between 
            ## left and right).  now I'm adding an item that makes my datastream 
            ## of odd length, which means that the median will be one of my vals
            
            ## is our new number in between the two edges?  if so, it's our new median
            if num >= self.left[-1] and num <= self.right[0]:
                self.median = num
                
            else:
                if num <= self.left[-1]:
                    insort(self.left, num)
                    self.median = self.left.pop()
                else:
                    insort(self.right, num)
                    self.median = self.right.pop(0)
                
        self.nitems += 1

    def findMedian(self) -> float:
        return self.median

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()