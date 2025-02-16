```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        s, e = 0, l(n) - 1 
        c_m = f("i")
        
        w s < e :
            m = s + (e - s) // 2
            c_m = m(c_m, n[m])
            i n[m] > n[e]:
                s = m + 1
            e:
                e = m - 1
        r m(c_m, n[s])

# Time Complexity: O(log N)
# Space Complexity: O(1)
```