# getattr()

# Returns the value of the named attribute of an object.

class MyClass:
    def __init__(self):
        self.name = 'John'

obj = MyClass()
print(getattr(obj, 'name'))  # Output: 'John'
