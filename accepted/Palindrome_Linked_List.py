## https://leetcode.com/problems/palindrome-linked-list/

## given a singly-linked list, determine if it's a palindrome

## kinda feels like cheating, but turn the linked list into a 
## regular list and then check if it's the same reversed.  

## results in O(n) time (though also O(n) space, which is less 
## ideal than requested).  stills ends up at 47.7th percentile in
## memory, and 81.9th percentile in runtime

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        l = head
        while l is not None:
            vals.append(l.val)
            l = l.next
        return vals == vals[::-1]