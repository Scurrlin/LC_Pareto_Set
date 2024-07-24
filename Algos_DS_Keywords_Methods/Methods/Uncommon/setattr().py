# setattr()

# Sets the value of the named attribute of an object.
class MyClass:
    def __init__(self):
        self.name = 'John'

obj = MyClass()
setattr(obj, 'name', 'Jane')
print(obj.name)  # Output: 'Jane'