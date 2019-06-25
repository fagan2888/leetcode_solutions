## https://leetcode.com/problems/populating-next-right-pointers-in-each-node

## problem is to add a pointer to each node in a complete binary tree that 
## points to the node to it's right.  solution is to create a list of nodes 
## at each level (takes O(N) time), then iterate over levels and make sure 
## those lists are sorted from left to right, then just add the pointers 
## appropriately.

## the initial tree walk takes O(N) time (touch each node once).  the 
## second walk takes O(L * (nlogn+n)), where L is the number of level and 
## n is the number of nodes in that level (since we have a sort plus an
## iteration over the sorted list).  since it's a complete binary 
## tree, L and n are related to N: L = ceil(log2(N)) and  n = 2^(L-1)


## runtime comes in at 84th percentile and memory comes in at 42nd 
## percentile (somewhat surprisingly)


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import defaultdict
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        nodes_by_level = defaultdict(list)
        
        todo = [(root, 0, 0)]
        while len(todo):
            node, level, lr = todo.pop()
            if node is None:
                continue
            
            nodes_by_level[level].append((node, lr))
            
            nextlevel = level + 1
            lradd = 1/(2**level)
            todo.append([node.left, nextlevel, lr-lradd])
            todo.append([node.right, nextlevel, lr+lradd])
        
        for level, nodelist in nodes_by_level.items():
            nodelist = sorted(nodelist, key=lambda x:  x[1])
            for ii, nodetup in enumerate(nodelist):
                if ii == len(nodelist) - 1:
                    nodetup[0].next = None
                else:
                    nodetup[0].next = nodelist[ii+1][0]
        
        return root