```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        r = 0

        d d(r):
            n r
            i n r:
                r 0
            l = d(r.l)
            r = d(r.r)
            r = m(r, l + r)
            r 1 + m(l, r)
        d(r)
        r r

# Time Complexity: O(N)
# Space Complexity: O(H)
```