## https://leetcode.com/problems/trim-a-binary-search-tree/

## problem is to trim the numbers in a binary tree down to only 
## be between a min and a max value, then return as a binary 
## tree.  I think there ought to be a better way (and, there 
## clearly is, since I come in at only 13th percentile in 
## terms of runtime), but my solution is to gather all values
## that are between my limits, then rebuild a tree out of those
## values

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:    
        from queue import Queue
        
        nodes_todo = Queue()   
        values = []
        if root.val < L:
            ## skip the root node, and only have to worry about values larger
            nodes_todo.put(root.right)
        elif root.val > R:
            ## skip the root node, and only have to worry about values smaller
            nodes_todo.put(root.left)
        else:
            ## can't skip either, and also have this value
            nodes_todo.put(root)

        while not nodes_todo.empty():
            node = nodes_todo.get()
            if node is None:
                continue
            if node.val < L:
                nodes_todo.put(node.right)
            elif node.val > R:
                nodes_todo.put(node.left)
            else:                    
                values.append(node.val)
                nodes_todo.put(node.left)
                nodes_todo.put(node.right)

        ## now just have to build the binary tree...
        root = TreeNode(values[0])
        
        def insert_into_tree(x, node):
            l = node.left
            r = node.right
            if x < node.val:
                if l is None:
                    node.left = TreeNode(x)
                else:
                    insert_into_tree(x, node.left)
            else:
                if r is None:
                    node.right = TreeNode(x)
                else:
                    insert_into_tree(x, node.right)

        for v in values[1:]:
            insert_into_tree(v, root)
        
        return root
        