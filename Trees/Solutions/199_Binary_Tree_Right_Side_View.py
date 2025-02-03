class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        v = []
        def dfs(node, level):
            if node:
                if level == len(v):
                    v.append(node.val)
                dfs(node.right, level + 1)
                dfs(node.left, level + 1)
                
        dfs(root, 0)
        return v

# v = view

# Time Complexity: O(N)
# Space Complexity: O(H)