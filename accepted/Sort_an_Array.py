## https://leetcode.com/problems/sort-an-array/

## problem is to sort an array.  obviously the solution 
## is return sorted(nums)...which comes in at 98th percentile, 
## probably because it's written in C in the backend

## but, the challenge is to write our own that will pass 
## the pseed and memory constraints.  awesome quick rundown 
## from https://www.interviewcake.com/sorting-algorithm-cheat-sheet:

#                    worst          best            average       space
# Selection Sort     O(n^2)         O(n^2)          O(n^2)        O(1)
# Insertion Sort     O(n^2)         O(n)            O(n^2)        O(1)
# Merge Sort         O(n\lg{n})     O(n\lg{n})      O(n\lg{n})    O(n)
# Quicksort          O(n^2)         O(n\lg{n})      O(n\lg{n})    O(\lg{n})
# Heapsort           O(n\lg{n})     O(n)            O(n\lg{n})    O(1)
# Counting Sort      O(n)           O(n)            O(n)          O(n)
# Radix Sort         O(n)           O(n)            O(n)          O(n)

# class TreeNode:
#     def __init__(self, val, parent=None, left=None, right=None):
#         self.val = val
#         self.parent = parent
#         self.left = left
#         self.right = right

# class MyMinHeap:
#     from copy import copy
#     def __init__(self, vals=[]):
#         self.root = None
#         for v in vals:
#             self.push(v)


#     def push(self, val):
#         if self.root is None:
#             self.root = TreeNode(val)
#             return

                    

#             ## need to put this new val above our root.
#             ## 3 (possible) ways to do that:
#             ## 1. set old root as left/right of new root with other empty
#             ## 2. check if left is none and right is not none, and 

#             if self.root.left is None:
#                 old_root = copy(self.root)
#                 new_root = TreeNode(val)
#                 self.root = new_root
#                 self.root.left = old_root
#             elif self.root.right is None:




class Solution:
    # merge sort is almost always a great option (i.e. worst is still n log n), 
    # and i've always found it relatively easy to understand, so I decided to go
    # with that first:

    ## this implementation comes in at only 7th percentile for runtime (428 ms)
    ## (though it is 65th percentile for memory, so not bad there).
    def merge_vals(self, vals1: List[int], vals2: List[int]) -> List[int]:
        l1 = len(vals1)
        if l1 == 0:
            return vals2
        
        l2 = len(vals2)
        if l2 == 0:
            return vals1
        
        out = []
        v1idx = 0
        v2idx = 0
        
        while True:
            if v1idx == len(vals1) and v2idx == len(vals2):
                break
            
            if v1idx == len(vals1):
                out.append(vals2[v2idx])
                v2idx = v2idx + 1
            elif v2idx == len(vals2):
                out.append(vals1[v1idx])
                v1idx = v1idx + 1
            
            else:
                if vals1[v1idx] <= vals2[v2idx]:
                    out.append(vals1[v1idx])
                    v1idx = v1idx + 1
                else:
                    out.append(vals2[v2idx])
                    v2idx = v2idx + 1
            
        return out

    def mergesort(self, nums: List[int]) -> List[int]:
        l = len(nums)
        if l < 2:
            return nums
        
        if l == 2:
            if nums[0] > nums[1]:
                return [nums[1], nums[0]]
            else:
                return nums
        
        else:
            from math import ceil
            split_point = int(ceil(l/2))
            vals1 = self.mergesort(nums[:split_point])
            vals2 = self.mergesort(nums[split_point:])
            out = self.merge_vals(vals1, vals2)
            return out                    
    
    ## I also find this a good chance to practice building a heap 
    ## though first, let's make sure I can do it using a heap:
    def heapsort(self, nums: List[int]) -> List[int]:
        from heapq import heapify
        minheap = heapify(nums)
        return [minheap.heappop() for ii in range(len(nums))]
        ## surprisingly, this still takes 

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums)
