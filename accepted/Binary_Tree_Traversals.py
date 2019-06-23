## https://leetcode.com/problems/binary-tree-inorder-traversal/
## https://leetcode.com/problems/binary-tree-postorder-traversal/
## https://leetcode.com/problems/binary-tree-preorder-traversal/

## I'm not doing the follow-ups for now, which are to do these in
## an interative fashion (which would be better for memory, since 
## your call stack doesn't go as deep).  however, these are nice
## and trivial to put together recursively, so here they are.

## speed and memory are all quite good
## at least, compared to what others are putting in

## method -- speed -- memory
## -------------------------
## inorder    80th      93rd
## postorder  99th      57th
## preorder   80th      98th

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ## inorder means (Left, Root, Right), not what I originally thought
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)        

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ## postorder is left, right, root:
        if root is None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ## preorder is: root, left, right
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
