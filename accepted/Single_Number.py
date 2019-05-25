## https://leetcode.com/problems/single-number/

## problem is to find the number in a list that
## appears only once.  could probably speed this 
## up with a sort, but not sure -- here we have a
## loop over the numbers and keep track of any 
## values that have only appeared once so far
## and then removing items from that set once we
## hit it a second time.  

## that should really be a set, not a list, since 
## I only care about the unique items.  that would 
## make the append/remove much faster...in fact, 
## overall, this entire algorithm is pretty slow!

## then, at the end, we return whatever item is
## left in the list of possible items

## we come in at 11th percentile in terms of runtime 
## and 21st in terms of memory


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        possible_options = []
        for item in nums:
            if item in count:
                count[item] += 1
                possible_options.remove(item)
            else:
                count[item] = 1
                possible_options.append(item)
        return possible_options[0]