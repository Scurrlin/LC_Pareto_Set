class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        view = []
        def dfs(node, level):
            if node:
                if level == len(view):
                    view.append(node.val)
                dfs(node.right, level + 1)
                dfs(node.left, level + 1)
                
        dfs(root, 0)
        return view