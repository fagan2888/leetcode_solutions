## https://leetcode.com/problems/majority-element/

## goal here is to find the one value in an array that appears more 
## then len(ar)/2 times.  we can assume this condition will always be
## satisfied by some element in the array.

## my solution is pretty simple -- use a hash table to keep track 
## of the count of each element, and break once we hit the count 
## we're looking for on some value (then return that value)

## gives us a worst-case runtime complexity of O(len(nums)), since
## each of lookups should be O(1) within the loop.

## that said, still comes in at 52nd percentile in runtime and 
## 16th in term of RAM, so could do better.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        curmax = -1
        curmax_val = None
        
        breakpoint = len(nums)/2 + 1
        
        for val in nums:
            if val in count:
                myc = count[val] + 1
            else:
                myc = 1
            
            count[val] = myc
            
            if myc > curmax:
                curmax = myc
                curmax_val = val
                        
            if curmax > breakpoint:
                break
        
        return curmax_val