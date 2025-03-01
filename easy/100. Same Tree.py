# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    ## Stack
        stackp, stackq = [], []
        currp = p
        currq = q
        
        while currp or currq or stackp:
            # checks whether one of currp or currq is None, but not both.
            # Sme as:
            # if currp is None and currq is not None:
            #     return False
            # elif currp is not None and currq is None:
            #     return False

            if (currp is None) != (currq is None): 
                return False
            # Traverse left subtree while keeping track of the structure
            while currp or currq:
                if (currp is None) != (currq is None): 
                    return False
                stackp.append(currp)
                stackq.append(currq)
                currp = currp.left if currp else None
                currq = currq.left if currq else None
            
            # Pop from stack and compare values
            currp = stackp.pop()
            currq = stackq.pop()
            
            if currp.val != currq.val:  # Values must be the same
                return False
            
            # Move to the right subtree
            currp = currp.right
            currq = currq.right
        
        return True



##Recursion (Better)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
            
        if p and q and p.val == q.val:
            # both left and right subtrees must be identical for the trees to be the same.
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # If one tree is None while the other is not, or if the values at p and q do not match
        return False
