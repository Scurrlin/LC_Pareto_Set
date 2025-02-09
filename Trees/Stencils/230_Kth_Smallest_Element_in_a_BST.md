```python
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        s = []
        c = r

        w s o c:
            w c:
                s.a(c)
                c = c.l
            c = s.p()
            k -= 1
            i k == 0:
                r c.v
            c = c.r
        
# Time Complexity: O(H + k)
# Space Complexity: O(H)
```