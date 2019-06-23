## https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/

## problem is just to traverse the tree and output all values sorted by their 
## level.  my solution is to do the standard traversal, but append outputs to 
## a dictionary that's level-by-level, then concatenate those levels together 
## at the end.

## does pretty well, coming in at 89th percentile for runtime (it is O(n), after
## all, though there's an extra factor of Nlevels we add in), but only 26th for 
## memory.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        output_by_level = {}
        nodes_todo_and_level = [(root, 0)]
        
        maxlevel = 0
        while len(nodes_todo_and_level):
            node, level = nodes_todo_and_level.pop()
            if level not in output_by_level:
                output_by_level[level] = [node.val]
            else:
                output_by_level[level].append(node.val)

            if node.right is not None:
                nodes_todo_and_level.append((node.right, level+1))
            if node.left is not None:
                nodes_todo_and_level.append((node.left, level+1))
            maxlevel = max(maxlevel, level)
        
        return [output_by_level[level] for level in range(maxlevel+1)]
        