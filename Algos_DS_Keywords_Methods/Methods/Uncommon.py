# __import__()
# ============
# This function is invoked by the import statement. It can be replaced in the __builtins__ module.

math = __import__('math')
print(math.sqrt(4))  # Output: 2.0

# ascii()
# =======
# Returns a string containing a printable representation of an object, but only
# uses ASCII characters.

print(ascii("Hello, 世界"))  # Output: 'Hello, \u4e16\u754c'

# breakpoint()
# ============
# Drops into the debugger at the call site. (Requires Python 3.7+)

breakpoint()  # Execution will stop here and drop into the debugger

# bytearray()
# ===========
# Returns a new array of bytes.

ba = bytearray([65, 66, 67])
print(ba)  # Output: bytearray(b'ABC')

# bytes()
# =======
# Returns a new "bytes" object, which is an immutable sequence of bytes.

b = bytes([65, 66, 67])
print(b)  # Output: b'ABC'

# callable()
# ==========
# Returns True if the object appears callable, False if not.

print(callable(print))  # Output: True
print(callable(42))     # Output: False

# classmethod()
# =============
# Returns a class method for the function.

class MyClass:
    @classmethod
    def my_class_method(cls):
        return 'class method called'

print(MyClass.my_class_method())  # Output: 'class method called'

# compile()
# =========
# Compiles source into a code or AST object.

code = compile('a = 5\nb = 6\nprint(a + b)', 'example', 'exec')
exec(code)  # Output: 11

# complex()
# =========
# Creates a complex number.

print(complex(1, 2))  # Output: (1+2j)
print(complex('1+2j'))  # Output: (1+2j)

# delattr()
# =========
# Deletes the named attribute from an object.

class MyClass:
    def __init__(self):
        self.name = 'John'

obj = MyClass()
delattr(obj, 'name')
print(hasattr(obj, 'name'))  # Output: False

# dir()
# =====
# Returns a list of the attributes and methods of any object.

print(dir(list))  # Output: [..., 'append', 'clear', 'copy', ...]

# divmod()
# ========
# Returns a tuple containing the quotient and the remainder when dividing two
# numbers.

# eval()
# ======
# Executes the passed string expression.

x = 1
print(eval('x + 1'))  # Output: 2

# exec()
# ======
# Executes the passed string or code object.

exec('a = 5\nprint(a)')  # Output: 5

# frozenset()
# ===========
# Returns a new frozenset object, optionally with elements taken from an
# iterable.

fs = frozenset([1, 2, 3, 2])
print(fs)  # Output: frozenset({1, 2, 3})

# getattr()
# =========
# Returns the value of the named attribute of an object.

class MyClass:
    def __init__(self):
        self.name = 'John'

obj = MyClass()
print(getattr(obj, 'name'))  # Output: 'John'

# globals()
# =========
# Returns a dictionary representing the current global symbol table.

print(globals())

# hasattr()
# =========
# Returns True if the object has the specified attribute.

class MyClass:
    def __init__(self):
        self.name = 'John'

obj = MyClass()
print(hasattr(obj, 'name'))  # Output: True

# hash()
# ======
# Returns the hash value of an object (if it has one).

print(hash('test'))  # Output: hash value (varies)

# help()
# ======
# Invokes the built-in help system.

help(print)

# isinstance()
# ============
# Returns True if the object is an instance of the class (or of a subclass
# thereof).

print(isinstance(5, int))  # Output: True
print(isinstance('hello', int))  # Output: False

# issubclass()
# ============
# Returns True if class is a subclass (direct, indirect or virtual) of
# classinfo.

class A:
    pass

class B(A):
    pass

print(issubclass(B, A))  # Output: True
print(issubclass(A, B))  # Output: False

# iter()
# ======
# Returns an iterator object.

my_list = [1, 2, 3]
it = iter(my_list)
print(next(it))  # Output: 1
print(next(it))  # Output: 2
print(next(it))  # Output: 3

# locals()
# ========
# Returns a dictionary representing the current local symbol table.

def func():
    a = 1
    print(locals())

func()  # Output: {'a': 1}

# memoryview()
# ============
# Returns a memory view object.

v = memoryview(b'abcd')
print(v[1])  # Output: 98
print(v[-1])  # Output: 100

# object()
# ========
# Returns a new featureless object.

obj = object()
print(obj)  # Output: <object object at ...>

# oct()
# =====
# Converts an integer to an octal string.

print(oct(8))  # Output: '0o10'

# open()
# ======
# Opens a file and returns a corresponding file object.

with open('test.txt', 'w') as f:
    f.write('Hello, World!')

# property()
# ==========
# Returns a property attribute.

class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

obj = MyClass(42)
print(obj.value)  # Output: 42

# repr()
# ======
# Returns a string containing a printable representation of an object.

print(repr('Hello, World!'))  # Output: "'Hello, World!'"

# setattr()
# =========
# Sets the value of the named attribute of an object.
class MyClass:
    def __init__(self):
        self.name = 'John'

obj = MyClass()
setattr(obj, 'name', 'Jane')
print(obj.name)  # Output: 'Jane'

# staticmethod()
# ==============
# Returns a static method for the function.

class MyClass:
    @staticmethod
    def my_static_method():
        return 'static method called'

print(MyClass.my_static_method())  # Output: 'static method called'

# super()
# =======
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

# vars()
# ======
# Returns the __dict__ attribute for a module, class, instance, or any other
# object with a __dict__ attribute.

class MyClass:
    def __init__(self):
        self.name = 'John'
        self.age = 30

obj = MyClass()
print(vars(obj))  # Output: {'name': 'John', 'age': 30}