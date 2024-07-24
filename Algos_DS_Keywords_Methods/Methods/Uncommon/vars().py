# vars()

# Returns the __dict__ attribute for a module, class, instance, or any other
# object with a __dict__ attribute.

class MyClass:
    def __init__(self):
        self.name = 'John'
        self.age = 30

obj = MyClass()
print(vars(obj))  # Output: {'name': 'John', 'age': 30}