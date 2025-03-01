class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper( rootl, rootr):
            if rootl is None and rootr is None: # if both none, return true
                return True
            # one none, one value + both none, but the first case exclude the situation of both none
            if not rootl or not rootr:
                return False
            elif rootl.val != rootr.val:
                return False
            else:
                return helper(rootl.left, rootr.right) and helper(rootl.right, rootr.left)
        return helper(root.left, root.right)
            