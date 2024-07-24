# classmethod()

# Returns a class method for the function.

class MyClass:
    @classmethod
    def my_class_method(cls):
        return 'class method called'

print(MyClass.my_class_method())  # Output: 'class method called'
