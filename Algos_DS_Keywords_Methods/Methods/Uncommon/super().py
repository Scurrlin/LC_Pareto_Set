# super()

# Returns a proxy object that delegates method calls to a parent or sibling
# class of type.

class Base:
    def hello(self):
        print("Hello from Base")

class Derived(Base):
    def hello(self):
        super().hello()
        print("Hello from Derived")

obj = Derived()
obj.hello()
# Output:
# Hello from Base
# Hello from Derived