## https://leetcode.com/problems/subtree-of-another-tree/

## it's not the prettiest solution, but it works and it doesn't 
## use much memory (83rd percentile there).  slow though -- only
## 5th percentile for runtime. 

## do it recursively -- if we hit a possible match (i.e. same values),
## then we call this function on the left and right subtrees.  if there
## are no left/right subtrees, we check that matches up with the tree
## that we're checking.  then we just need to handle our base cases.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode, check_single=False) -> bool:
        if t is None:
            if check_single:
                return (s is None)
            else:
                return True
        
        from collections import deque
        nodes_todo = deque([s])
        while len(nodes_todo):
            node = nodes_todo.popleft()
            if node is None:
                if t is None:
                    return True
                elif check_single:
                    return False
                else:
                    continue
                
            ## possible match!
            if node.val == t.val:
                ## check left and right are a match as well, and return true if so
                if node.left is None and node.right is None:
                    if (t.left is None and t.right is None):
                        return True
                elif node.left is None:
                    if (t.left is None) and self.isSubtree(node.right, t.right, check_single=True):
                        return True
                elif node.right is None:
                    if (t.right is None) and self.isSubtree(node.left, t.left, check_single=True):
                        return True
                else:
                    if (self.isSubtree(node.left, t.left, check_single=True) and self.isSubtree(node.right, t.right, check_single=True)):
                        return True
            
            ## if we got this far, then node was not a valid subtree, so check it's subtrees if we're allowed
            if check_single:
                ## if we're not allowed to check subtrees, return False
                return False
                
            if node.left is not None:
                nodes_todo.append(node.left)
            if node.right is not None:
                nodes_todo.append(node.right)
        
        ## if we get this far, then we didn't find it
        return False