class Solution:
    def cloneGraph(self, node: "Node") -> "Node":

        # Hash map to store original-to-clone mapping
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:

                # Return already cloned node
                return oldToNew[node]

            # Create a new node copy
            copy = Node(node.val)

            # Map original node to the cloned node
            oldToNew[node] = copy

            # Recursively clone all neighbors
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))

            # Return the cloned node    
            return copy

        # Handle empty graph case
        return dfs(node) if node else None

# Time Complexity: O(N + E)
# Space Complexity: O(N)