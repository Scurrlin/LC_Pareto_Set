class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        # Both trees are empty, so they are the same
        if not p and not q:
            return True
        
        # Both nodes exist and have the same value
        if p and q and p.val == q.val:

            # Recursively check left and right subtrees
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:

            # Trees differ in structure or values
            return False

# Time Complexity: O(N)
# Space Complexiy: O(H)