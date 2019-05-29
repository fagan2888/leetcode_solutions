## https://leetcode.com/problems/merge-two-sorted-lists/

## merge two sorted linked lists.  pretty simple solution here, 
## but about as fast as you can get.  initiate the list by checking
## for the smaller of the two heads (or, if one is None, just use the
## other), then we iterate as long as we have either value and add the
## smaller of the two (or the only of the two, if one is None)

## therefore, it's just O(len(l1)+len(l2)).  96th percentile in runtime.
## only 16th percentile in memory somehow...dunno how you can do better 
## there, but whatever

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
               
        if l1 is None:
            out_head = l2
            l2 = l2.next
        elif l2 is None:
            out_head = l1
            l1 = l1.next        
        elif l1.val < l2.val:
            out_head = l1
            l1 = l1.next
        else:
            out_head = l2
            l2 = l2.next
        
        out = out_head
        while l1 is not None or l2 is not None:
            if l1 is None:
                out.next = l2
                l2 = l2.next
            elif l2 is None:
                out.next = l1
                l1 = l1.next
            else:
                if l1.val < l2.val:
                    out.next = l1
                    l1 = l1.next
                else:
                    out.next = l2
                    l2 = l2.next
            out = out.next
        return out_head
        