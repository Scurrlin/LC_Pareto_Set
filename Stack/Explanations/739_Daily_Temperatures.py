class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Alias for readability
        T = temperatures

        # Initialize result list with 0s
        res = [0] * len(T)

        # Monotonic decreasing stack (stores indices)
        stack = []

        # Iterate through temperatures
        for i, t in enumerate(T):

            # Warmer day found
            while stack and t > T[stack[-1]]:

                # Get index of previous cooler day
                index = stack.pop()

                # Compute days difference
                res[index] = i - index

            # Store current index in stack
            stack.append(i)
        
        # Return the result list
        return res

# Time Complexity: O(N)
# Space Complexity: O(N)