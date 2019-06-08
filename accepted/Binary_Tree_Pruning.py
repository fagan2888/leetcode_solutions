## https://leetcode.com/problems/binary-tree-pruning/

## not the prettiest solution to this problem since it involves
## two iterations over the tree, but it's cleaner and easier
## to understand what's happening by doing it this way.  we 
## also make use of the functools lru_cache decorator to substantially 
## speed up the recursive calculation -- with it, we get ~36 ms, 89th 
## percentile for runtime.  without it, we get 48ms, 17th percentile
## for runtime.  of course, there's a tradeoff with memory, where
## implementing the cache takes us from 50th percentile to 5th percentile.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from functools import lru_cache

class Solution:
    
    @lru_cache(None)
    def values_below(self, node: TreeNode) -> List:
        out = [node.val]
        if node.left is not None:
            out += self.values_below(node.left)
        if node.right is not None:
            out += self.values_below(node.right)
        return out        

    def pruneTree(self, root: TreeNode) -> TreeNode:
        from collections import deque
        todo = deque([root])
        while len(todo):
            node = todo.popleft()
            node.vals_below = self.values_below(node)
            if 1 not in node.vals_below:
                node.keep = False
            else:
                node.keep = True
                if node.left is not None:
                    todo.append(node.left)
                if node.right is not None:
                    todo.append(node.right)           

        if root.keep == False:
            return None
                    
        todo = deque([root])
        while len(todo):
            node = todo.popleft()
            if node is None:
                continue            
            if node.left is not None and not node.left.keep:
                node.left = None
            elif node.left is not None:
                todo.append(node.left)
            
            if node.right is not None and not node.right.keep:
                node.right = None
            elif node.right is not None:
                todo.append(node.right)
        
        return root
        