## https://leetcode.com/problems/n-ary-tree-preorder-traversal/

## pretty straightforward solution here -- add on to a list and pop
## from the end so I do all the children of a node before I move on 
## to the next node at the same level.  only caveat is that for some
## reason the order of the children is inverted from what I want, so 
## flip it around.

## runtime is fine -- between 94th percentile and 14th percentile.
## memory is also good at 47th percentile


"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        vals = []
        todo = [root]
        while len(todo):
            node = todo.pop()
            if node is None:
                continue

            vals.append(node.val)
            todo.extend(node.children[::-1])
            ## done with the node at this point, so delete it to save memory
            del node
        return vals