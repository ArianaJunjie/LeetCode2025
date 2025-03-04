class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return 0
            left_depth = helper(root.left)
            right_depth = helper(root.right)
            if left_depth == -1 or right_depth == -1 or abs(left_depth - right_depth) > 1:
                return -1 # return -1 if a subtree is unbalanced
            else:
                return 1 + max(left_depth, right_depth)
        return helper(root) != -1