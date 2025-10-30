```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        o = [1] * l(n)
        
        l = 1
        f i i r(l(n)):
            o[i] *= l
            l *= n[i]
            
        r = 1
        f i i r(l(n) - 1, -1, -1):
            o[i] *= r
            r *= n[i]

        r o

# Time Complexity: O(N)
# Space Complexity: O(N)
```