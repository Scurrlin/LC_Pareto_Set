class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Stores the maximum profit
        res = 0

        # Initialize lowest price seen so far
        lowest = prices[0]

        for p in prices:

            # Update lowest price if current price is lower
            if p < lowest:
                lowest = p

            # Calculate profit and update max profit if higher
            res = max(res, p - lowest)

        # Return max profit found
        return res

# Time Complexity: O(N)
# Space Complexity: O(1)