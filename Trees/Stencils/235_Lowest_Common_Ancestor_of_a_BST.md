```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        w T:
            i r.v < p.v a r.v < q.v:
                r = r.r
            e r.v > p.v a r.v > q.v:
                r = r.l
            e:
                r r

# Time Complexity: O(H)
# Space Complexity: O(1)
```