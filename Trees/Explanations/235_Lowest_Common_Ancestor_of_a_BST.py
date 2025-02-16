class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:

            # If both nodes are in the right subtree
            if root.val < p.val and root.val < q.val:
                root = root.right

            # If both nodes are in the left subtree
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:

                # Found the LCA (split point where p and q diverge)
                return root

# Time Complexity: O(H)
# Space Complexity: O(1)