class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:

            # Return empty list for an empty tree
            return []
        
        # Stores the rightmost node at each level
        v = []
        def dfs(node, level):
            if node:

                # First node encountered at this level
                if level == len(v):
                    v.append(node.val)

                # Traverse right subtree first    
                dfs(node.right, level + 1)

                # Then traverse left subtree
                dfs(node.left, level + 1)
                
        # Start DFS from the root at level 0
        dfs(root, 0)

        # Return the collected right-side view nodes
        return v

# v = view

# Time Complexity: O(N)
# Space Complexity: O(H)