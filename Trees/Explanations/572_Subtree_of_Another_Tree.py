class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot == None:

            # An empty subRoot is always a subtree
            return True

        if root == None:

            # If root is empty but subRoot is not, it can't be a subtree
            return False

        # Check if current tree is identical to subRoot
        if self.same(root, subRoot):
            return True
        
        # Recursively check left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)            

    def same(self, r, s):
        if r == None and s == None:

            # Both trees are empty, so they are the same
            return True

        # Compare values and recursively check children
        if r and s and r.val == s.val:
            return self.same(r.right, s.right) and self.same(r.left, s.left)

# Time Complexity: O(N x M)
# Space Complexity: O(H)