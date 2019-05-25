## https://leetcode.com/problems/insert-into-a-binary-search-tree/

## insert a value into an existing binary search tree.  pretty 
## straightforward -- walk the tree until we find an empty node 
## where we would put the val, then create a node there

## that means our runtime is going to be height of the tree at 
## worst.  comes in at 81st percentile in terms of runtime and 
## 83rd in terms of memory

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        while True:
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
                    continue
            
            if val > node.val:
                if node.right is None:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
                    continue