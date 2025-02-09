```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        r = []
        
        d d(n, l):
            i n n:
                r
            i l(r) <= l:
                r.a([])
            r[l].a(n.v)
            d(n.l, l + 1)
            d(n.r, l + 1)

        d(r, 0)
        r r

# Time Complexity: O(N)
# Space Complexity: O(H)
```