## https://leetcode.com/problems/next-greater-node-in-linked-list/

## given a single-linked list, problem is to find the next value
## in that list (for each entry) that is larger than that entry.

## this solution is too slow still though.  we try to re-use previous 
## answers (i.e. if the previous value is larger than my value, then 
## the answer for myself is the same as the answer for that one)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        def get_next_greater(node, x):
            if node is None:
                return 0
            if node.val > x:
                return node.val
            return get_next_greater(node.next, x)
    
        node = head
        answer = []
        previous_answer = None
        previous_value = None
        while node is not None:
            if previous_answer is not None:
                if previous_answer == node.val or node.val < previous_value:
                    ## if we hit the previous answer or found a smaller number, 
                    ## then we need to reset
                    previous_answer = get_next_greater(node.next, node.val)
                    previous_value = node.val
                    answer.append(previous_answer)
                    node = node.next
                    continue
                elif previous_answer > node.val:
                    ## if the previous answer is larger than this value, 
                    ## then it's also the answer for this value
                    answer.append(previous_answer)
                    previous_value = node.val
                    node = node.next
                    continue
                    
            ## all other cases -- either don't have a previous
            ## answer or this value is larger than the previous answer
            ## so find the answer for this one and save it
            previous_answer = get_next_greater(node.next, node.val)
            previous_value = node.val
            answer.append(previous_answer)
            node = node.next
        return answer
