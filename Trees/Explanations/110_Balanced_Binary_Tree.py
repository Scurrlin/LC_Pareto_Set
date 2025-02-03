class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:

                # Base case: empty tree is balanced with height 0
                return [True, 0]

            # Recursion for left and right subtrees
            left, right = dfs(root.left), dfs(root.right)

            # Check balance condition
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            
            # Return balance status and height
            return [balanced, 1 + max(left[1], right[1])]

        # Return whether the tree is balanced
        return dfs(root)[0]

# Time Complexity: O(N)
# Space Complexity: O(H)