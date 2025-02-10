```python
class Solution:
    def reorderList(self, head: ListNode) -> None:
        i n h o n h.n:
            r
        s, f = h, h.n
        
        w f a f.n:
            s = s.n
            f = f.n.n
        s = s.n
        p = s.n = N
        w s:
            t = s.n
            s.n = p
            p = s
            s = t
        f, s = h, p
        w s:
            t, t = f.n, s.n
            f.n = s
            s.n = t
            f, s = t, t

# Time Complexity: O(N)
# Space Complexity: O(1)
```