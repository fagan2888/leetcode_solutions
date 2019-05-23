## https://leetcode.com/problems/range-sum-of-bst/

## pretty simple solution -- use a queue to keep track
## of the nodes I still have to touch.  nodes that are 
## within my range get added and have their left and right
## added to that queue.  nodes that are above only get their
## left added and vice versa.

## comes in at 92nd percentile in runetime but only 8th in 
## memory.  queue takes up a (relatively) large amount of memory.

## worst case runtime complexity is O(N), where N is the number 
## of nodes in the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        from collections import deque
        nodes_to_touch = deque([root])
        total = 0
        
        while len(nodes_to_touch):
            node = nodes_to_touch.popleft()
            if node is None:
                continue
            
            if L <= node.val <= R:  
                total = total + node.val
                nodes_to_touch.append(node.left)
                nodes_to_touch.append(node.right)
            
            elif node.val > R:
                ## bigger than the allowed biggest value -- only check the nodes to the left
                nodes_to_touch.append(node.left)
            elif node.val < L:
                ## smaller than the allowed smallest -- only check to the right
                nodes_to_touch.append(node.right)
        
        return total