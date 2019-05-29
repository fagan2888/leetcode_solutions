## https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/

## problem is to remove the nth item from the end of a linked list.  follow-up
## is to do this in one pass, but I'm not positive how to do that right now, so 
## i'll do it the easier to understand but slower way (comes in at 18th percentile
## for runtime, though 84th for memory)

## that means we iterate over it to get the length, then figure out which node
## we're removing based on that, then re-assign the linking as appropriate 
## or, if we're deleting the head, we just return the head's next link

## worst-case scenario is therefore O(2*n) since we have to with a min of 
## O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        ## tackle it w/o the follow-up at first
        length = 0
        l = head
        while l is not None:
            length = length + 1
            l = l.next
            
        target = length - n
        idx = 0
        l = head
        prev_l = None
        while idx < target:
            prev_l = l
            l = l.next
            idx = idx + 1
            
        if prev_l is None:
            return l.next
        else:
            prev_l.next = l.next
            return head
        