class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        b_map = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in b_map.values():
                stack.append(char)
            elif char in b_map.keys():
                if not stack or b_map[char] != stack.pop():
                    return False
        return not stack
        
# b_map = bracket_map

# Time Complexity: O(N)
# Space Complexity: O(N)