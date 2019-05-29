## https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

## problem is this:  given a binary tree (specified by the root), and 
## two nodes in that tree, find the lowest common ancestor of those two 
## nodes.  

## my solution, which i thought would be too slow but which isn't, is to 
## invert the tree (i.e. assign a parent node to each node), then build a 
## list of ancestors of p (which includes p), then word my way up the q
## ancestor branch until I find an overlapping node, then return that node

## the inversion step is O(n), since I touch each node once.  the tree walks
## are O(log(n)) each at worst, which is when both nodes are at opposite sides 
## of the bottom of the tree.  the q walk also adds a lookup of the length of
## the p branch, which again is log(n) in worst case, for each iteration.

## so putting it all together, we have O(n + log(n) + log(n)*log(n)), where the
## *log(n) is because the max length of the list of p ancestors is log(n)
## (and lookup in a list is worst-case length of that list).

## definitely still dominated by the inversion step.  this solution comes in 
## at almost 98th percentile in terms of runtime and almost 89th percentile 
## in terms of memory, so it's doing very well

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ## I'm probably wrong, but intuitively it seems like the fastest would be to assign 
        ## parents to each node (going top down), then work my way back up from p and q until
        ## I find an ancestor in common
        
        from collections import deque
        nodes_to_touch = deque([root])
        
        root.parent = None
        while len(nodes_to_touch):
            node = nodes_to_touch.popleft()
            if node.left is not None:
                node.left.parent = node
                nodes_to_touch.append(node.left)
            if node.right is not None:
                node.right.parent = node
                nodes_to_touch.append(node.right)
        
        ## now build the ancestors of p
        p_ancestors = [p]
        while p_ancestors[-1].parent is not None:
            p_ancestors.append(p_ancestors[-1].parent)
        
        q_ancestors = [q]
        while q_ancestors[-1] not in p_ancestors:
            q_ancestors.append(q_ancestors[-1].parent)
        
        return q_ancestors[-1]