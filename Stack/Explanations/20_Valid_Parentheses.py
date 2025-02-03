class Solution:
    def isValid(self, s: str) -> bool:

        # Stack to store opening brackets
        stack = []

        # Bracket mapping for closing brackets
        b_map = {")":"(", "}":"{", "]":"["}

        for char in s:

            # If it's an opening bracket, push to stack
            if char in b_map.values():
                stack.append(char)

            # If it's a closing bracket
            elif char in b_map.keys():

                # Check for a valid match
                if not stack or b_map[char] != stack.pop():
                    return False
                
        # Stack should be empty if all brackets matched
        return not stack
        
# b_map = bracket_map

# Time Complexity: O(N)
# Space Complexity: O(N)