```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = s()
        l = 0
        r = 0

        f r i r(l(s)):
            w s[r] i c:
                c.r(s[l])
                l += 1
            c.a(s[r])
            r = m(r, r - l + 1)
        r r

# Time Complexity: O(N)
# Space Complexity: O(1)
```