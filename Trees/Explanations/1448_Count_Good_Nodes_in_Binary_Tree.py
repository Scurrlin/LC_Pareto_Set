class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val: int) -> int:
            if not node:

                # Base case: no node to process
                return 0
            
            # Count of good nodes in this subtree
            count = 0

            # If current node is a "good node"
            if node.val >= max_val:
                count += 1

                # Update max_val to the current node value
                max_val = node.val

            # Recursion for left subtree    
            count += dfs(node.left, max_val)

            # Recursion for right subtree
            count += dfs(node.right, max_val)

            # Return total count of good nodes in this subtree
            return count
        
        # Start DFS with initial max_val as negative infinity
        return dfs(root, float('-inf'))

# Time Complexity: O(N)
# Space Complexity: O(H)