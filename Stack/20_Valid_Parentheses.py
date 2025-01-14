class Solution:
    def isValid(self, s):
        stack = []
        b_map = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in b_map:
                top_element = stack.pop() if stack else '#'
                if b_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

# b_map = bracket_map