class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0
            count = 0
            if node.val >= max_val:
                count += 1
                max_val = node.val
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)
            return count
        
        return dfs(root, float('-inf'))

# Time Complexity: O(N)
# Space Complexity: O(H)