class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # Stores level-order traversal result
        res = []
        
        def dfs(node, level):
            if not node:

                # Base case: return if node is None
                return
            if len(res) <= level:

                # Create a new list for this level
                res.append([])

            # Add node's value to its level
            res[level].append(node.val)

            # Traverse left subtree
            dfs(node.left, level + 1)

            # Traverse right subtree
            dfs(node.right, level + 1)

        # Start DFS from root at level 0
        dfs(root, 0)
        
        # Return level-order traversal
        return res

# Time Complexity: O(N)
# Space Complexity: O(H)