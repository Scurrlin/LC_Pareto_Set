```python
class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        o = {}

        d d(n):
            i n i o:
                r o[n]
            c = N(n.v)
            o[n] = c
            f n i n.n:
                c.n.a(d(n))
            r c
        r d(n) i n e N

# Time Complexity: O(N + E)
# Space Complexity: O(N)
```