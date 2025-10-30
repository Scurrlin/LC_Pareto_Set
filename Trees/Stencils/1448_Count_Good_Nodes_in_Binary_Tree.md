```python
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        d d(n: T, m_v: i) -> i:
            i n n:
                r 0
            
            c = 0
            i n.v >= m:
                c += 1
                m = n.v
            c += d(n.l, m)
            c += d(n.r, m)
            r c
        r d(r, f('-i'))

# Time Complexity: O(N)
# Space Complexity: O(H)
```