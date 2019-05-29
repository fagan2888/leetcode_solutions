## https://leetcode.com/problems/add-two-numbers/

## given two linked-lists where the values of the nodes represent 
## an integer in reverse order (i.e. [5, 0, 3] -> 305), add them
## together and return in the same way.

## my solution is to build a string out of the values, then convert
## it to an integer (so O(len(l1) + len(l2))), add them up, then 
## build the inverse (so O(len(out))), where len here is the number
## of digits in base 10

## comes in at 67th percentile for runtime and 83rd for memory

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def get_number(self, l1: ListNode) -> int:
        out = ''
        l = l1
        while l is not None:
            out += str(l.val)
            l = l.next
        return int(out[::-1])
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = self.get_number(l1)
        n2 = self.get_number(l2)
        
        val = str(n1 + n2)[::-1]
        
        out_head = ListNode(val[0])
        l = out_head
        for ii in range(1, len(val)):
            l.next = ListNode(val[ii])
            l = l.next
        return out_head
        