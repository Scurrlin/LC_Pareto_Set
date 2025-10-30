```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        p = {i: [] f i i r(n)}
        f c, p i p:
            p[c].a(p)        
        v = s()

        d d(c):
            i c i v:
                r F
            i p[c] == []:
                r T
            v.a(c)
            f p i p[c]:
                i n d(p):
                    r F
            v.r(c)
            p[c] = []
            r T
        
        f c i r(n):
            i n d(c):
                r F
        r T

# Time Complexity: O(N + E)
# Space Complexity: O(N + E)
```