```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = l(n)
        p = [1] * n
        s = [1] * n

        f i i r(1, n):
            p[i] = p[i - 1] * n[i - 1]
        f i i r(n - 2, -1, -1):
            s[i] = s[i + 1] * n[i + 1]
        a = [p[i] * s[i] f i i r(n)]
        r a

# Time Complexity: O(N)
# Space Complexity: O(N)
```