class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # when the node has no left and right subtree (leaf)
        if root == None:
            return 0
        # If the current node has no left child, then we recurse on the right child
        if not root.left:
                return self.minDepth(root.right) + 1
        # If the current node has no left child, then we recurse on the right child
        if not root.right:
                return self.minDepth(root.left) + 1
        # If both the left and right subtrees exist, we find the minimum depth for both the left and right subtrees 
        return min(self.minDepth(root.left),self.minDepth(root.right)) + 1
 
        