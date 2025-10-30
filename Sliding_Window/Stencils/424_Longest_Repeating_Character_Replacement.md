```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = {}
        l, m = 0, 0

        f r i r(l(s)):
            c[s[r]] = 1 + c.g(s[r], 0)
            m = m(m, c[s[r]])
            i (r - l + 1) - m > k:
                c[s[l]] -= 1
                l += 1
        r (r - l + 1)

# Time Complexity: O(N)
# Space Complexity: O(1)
```