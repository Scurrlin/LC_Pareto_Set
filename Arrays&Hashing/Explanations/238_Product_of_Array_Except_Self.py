class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Prefix products
        p = [1] * n

        # Suffix products
        s = [1] * n

        # Compute prefix products
        for i in range(1, n):
            p[i] = p[i - 1] * nums[i - 1]
        
        # Compute suffix products
        for i in range(n - 2, -1, -1):
            s[i] = s[i + 1] * nums[i + 1]
        
        # Compute final answer by multiplying prefix and suffix products
        answer = [p[i] * s[i] for i in range(n)]
        return answer

# Time Complexity: O(N)
# Space Complexity: O(N)