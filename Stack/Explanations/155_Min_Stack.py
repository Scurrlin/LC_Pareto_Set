class MinStack:
    def __init__(self):

        # Standard stack to store all values
        self.stack = []

        # Auxiliary stack to track min values
        self.minStack = []

    def push(self, val: int) -> None:

        # Push value to main stack
        self.stack.append(val)

        # Push the min value so far into minStack
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:

        # Remove top element from main stack
        self.stack.pop()

        # Remove corresponding min value
        self.minStack.pop()

    def top(self) -> int:

        # Return top element of main stack
        return self.stack[-1]

    def getMin(self) -> int:

        # Return top of minStack (current min value)
        return self.minStack[-1]

# Time Complexity: O(1)
# Space Complexity: O(N)