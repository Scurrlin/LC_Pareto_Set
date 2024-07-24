# hasattr()

# Returns True if the object has the specified attribute.

class MyClass:
    def __init__(self):
        self.name = 'John'

obj = MyClass()
print(hasattr(obj, 'name'))  # Output: True
