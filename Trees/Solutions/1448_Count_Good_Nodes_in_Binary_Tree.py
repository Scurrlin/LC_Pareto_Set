class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, maxVal: int) -> int:
            if not node:
                return 0
            
            count = 0
            if node.val >= maxVal:
                count += 1
                maxVal = node.val
            count += dfs(node.left, maxVal)
            count += dfs(node.right, maxVal)
            return count
        return dfs(root, float('-inf'))

# Time Complexity: O(N)
# Space Complexity: O(H)