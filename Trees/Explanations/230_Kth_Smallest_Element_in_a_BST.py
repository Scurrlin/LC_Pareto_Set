class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        # Stack for iterative in-order traversal
        stack = []

        # Start from the root node
        curr = root

        while stack or curr:

            # Traverse to the leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left

            # Process the leftmost node    
            curr = stack.pop()

            # Decrement k as we visit each node
            k -= 1
            if k == 0:

                # Return the k-th smallest element
                return curr.val
            
            # Move to the right subtree
            curr = curr.right

# Time Complexity: O(H + k)
# Space Complexity: O(H)