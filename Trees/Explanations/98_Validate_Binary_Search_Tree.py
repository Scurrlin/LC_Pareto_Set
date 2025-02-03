class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Stack for in-order traversal, prev for tracking last visited node
        stack, prev = [], float("-inf")

        while root or stack:

            # Traverse left subtree
            while root:
                stack.append(root)
                root = root.left

            # Process the node
            root = stack.pop()

            # Check if the BST property is violated
            if root.val <= prev:
                return False
            
            # Update prev to current node's value
            prev = root.val

            # Move to right subtree

            root = root.right

        # If all nodes are in order, it's a valid BST
        return True

# Time Complexity: O(N)
# Space Complexity: O(H)