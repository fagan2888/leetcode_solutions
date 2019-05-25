## https://leetcode.com/problems/search-in-a-binary-search-tree/

## kinda a classic problem I guess -- search a node with a given value
## in a binary search tree, or return none if there aren't any

## here our worst-case runtime is the height of the tree, so we come
## in at 82nd percentile there and 25th percentile in terms of memory

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        while True:
            if node.val == val:
                return node
            
            elif val < node.val:
                if node.left is not None:
                    node = node.left
                    continue
                else:
                    return
            
            else:
                if node.right is not None:
                    node = node.right
                    continue
                else:
                    return