## Stack
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Step 1: curr = root (1), push 1 to stack → stack = [1]
        # Step 2: curr = curr.left, but 1 has no left child → curr = None
        # Step 3: Pop from stack (1), visit it → res = [1]
        # Step 4: Move to curr.right (curr = 2), push 2 to stack → stack = [2]
        # Step 5: Move to curr.left (curr = 3), push 3 to stack → stack = [2, 3]
        # Step 6: curr = curr.left, but 3 has no left child → curr = None
        # Step 7: Pop from stack (3), visit it → res = [1, 3]
        # Step 8: Move to curr.right, but 3 has no right child → curr = None
        # Step 9: Pop from stack (2), visit it → res = [1, 3, 2]
        # Step 10: Move to curr.right, but 2 has no right child → curr = None
        # Step 11: Stack is empty, exit loop → Final Output: [1, 3, 2]

        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop() # pop until the stack is empty
            res.append(curr.val)
            curr = curr.right
        return res
    
## Recursion
class Solution:
    def inorderTraversal(self, root):
        res = []
        self.helper(root, res) 
        return res

    def helper(self, root, res):
        if root is not None:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)