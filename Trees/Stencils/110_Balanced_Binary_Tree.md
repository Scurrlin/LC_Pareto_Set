```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        d d(r):
            i n r:
                r [T, 0]

            l, r = d(r.l), d(r.r)
            b = l[0] a r[0] a a(l[1] - r[1]) <= 1
            r [b, 1 + m(l[1], r[1])]
        r d(r)[0]

# Time Complexity: O(N)
# Space Complexity: O(H)
```