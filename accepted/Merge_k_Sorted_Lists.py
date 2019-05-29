## https://leetcode.com/problems/merge-k-sorted-lists/

## merge k sorted linked lists into one sorted linked list.

## my method barely passed (16th percentile, though 44th in memory),
## but it does pass. i build a list of values, then keep finding the
## smallest, adding that list to my output then moving it forward, 
## then deleting any nones or updating non-nones.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:                
        ## remove any blank lists:
        new_lists = [l for l in lists if l is not None]
        lists = new_lists

        if not len(lists):
            return None
        
        vals = [l.val for l in lists]        
        idx = vals.index(min(vals))
        out_head = lists[idx]
        
        lists[idx] = lists[idx].next
        if lists[idx] is None:
            del lists[idx]
            del vals[idx]
        else:
            vals[idx] = lists[idx].val

        out = out_head
        while len(lists):
            idx = vals.index(min(vals))            
            out.next = lists[idx]
            out = out.next
            
            lists[idx] = lists[idx].next
            if lists[idx] is None:
                del lists[idx]
                del vals[idx]
            else:
                vals[idx] = lists[idx].val

        return out_head
