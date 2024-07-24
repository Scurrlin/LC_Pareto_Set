# delattr()

# Deletes the named attribute from an object.

class MyClass:
    def __init__(self):
        self.name = 'John'

obj = MyClass()
delattr(obj, 'name')
print(hasattr(obj, 'name'))  # Output: False
