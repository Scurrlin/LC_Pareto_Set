class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack, prev = [], float("-inf")

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True

# Time Complexity: O(N)
# Space Complexity: O(H)