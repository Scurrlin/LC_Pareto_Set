class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        T = temperatures
        res = [0] * len(T)
        stack = []

        for i, t in enumerate(T):
            while stack and t > T[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res

# Time Complexity: O(N)
# Space Complexity: O(N)