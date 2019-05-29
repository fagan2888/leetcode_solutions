## https://leetcode.com/problems/linked-list-cycle/

## very poorly stated/described problem, but basically 
## there may or may not be a node that points back to a
## previous node in a list.  find out whether or not there
## is.

## i accomplish this by keeping a set of my past nodes
## so that I have O(1) lookup of my past nodes.  that means
## i ignore the followup to do it in constant memory though.

## comes in much faster though, at 97th percentile, but only
## 17th percentile in memory.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        
        past_nodes = set([head])
        n = head
        while n.next is not None:
            n = n.next
            if n in past_nodes:
                return True
            past_nodes.add(n)
        return False