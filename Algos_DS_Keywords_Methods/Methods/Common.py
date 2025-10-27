# abs()
# =====
# Returns the absolute value of a number.

print(abs(-7))  # Output: 7
print(abs(3.14))  # Output: 3.14

# all()
# =====
# Returns True if all elements of an iterable are true (or if the iterable is
# empty).

print(all([1, 2, 3]))  # Output: True
print(all([0, 1, 2]))  # Output: False

# any()
# =====
# Returns True if any element of an iterable is true. If the iterable is empty,
# return False.

print(any([0, 1, 2]))  # Output: True
print(any([0, 0, 0]))  # Output: False

# bin()
# =====
# Converts an integer to a binary string.

print(bin(10))  # Output: '0b1010'

# bool()
# ======
# Converts a value to a Boolean, using the standard truth testing procedure.

print(bool(0))  # Output: False
print(bool(1))  # Output: True

# chr()
# =====
# Returns the string representing a character whose Unicode code point is the
# integer.

print(chr(97))  # Output: 'a'
print(chr(8364))  # Output: '€'

# dict()
# ======
# Creates a new dictionary.

d = dict(a=1, b=2)
print(d)  # Output: {'a': 1, 'b': 2}

# enumerate()
# ===========
# Adds a counter to an iterable and returns it as an enumerate object.

for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)

# Output:
# 0 a
# 1 b
# 2 c

# filter()
# ========
# Constructs an iterator from elements of an iterable for which a function
# returns true.

def is_even(n):
    return n % 2 == 0
result = filter(is_even, [1, 2, 3, 4])
print(list(result))  # Output: [2, 4]

# float()
# =======
# Converts a number or string to a floating point number.

print(float(10))  # Output: 10.0
print(float('3.14'))  # Output: 3.14

# format()
# ========
# Returns a formatted representation of a value.

print(format(1234, '0>10'))  # Output: '0000001234'
print(format(3.14159, '.2f'))  # Output: '3.14'

# hex()
# =====
# Converts an integer to a hexadecimal string.

print(hex(255))  # Output: '0xff'

# id()
# ====
# Returns the identity of an object.

a = 42
print(id(a))  # Output: unique id of a

# input()
# =======
# Reads a line from input, converts it to a string.

name = input('Enter your name: ')
print(f'Hello, {name}!')

# int()
# =====
# Converts a number or string to an integer.

print(int(3.14))  # Output: 3
print(int('42'))  # Output: 42

# len()
# =====
# Returns the length (the number of items) of an object.

print(len('hello'))  # Output: 5
print(len([1, 2, 3]))  # Output: 3

# list()
# ======
# Returns a list.

print(list('hello'))  # Output: ['h', 'e', 'l', 'l', 'o']

# map()
# =====
# Applies a function to every item of an iterable and returns a list of the results.

def square(n):
    return n * n
result = map(square, [1, 2, 3, 4])
print(list(result))  # Output: [1, 4, 9, 16]

# max()
# =====
# Returns the largest item in an iterable or the largest of two or more
# arguments.

print(max(1, 2, 3))  # Output: 3
print(max([1, 2, 3]))  # Output: 3

# min()
# =====
# Returns the smallest item in an iterable or the smallest of two or more
# arguments.

print(min(1, 2, 3))  # Output: 1
print(min([1, 2, 3]))  # Output: 1

# next()
# ======
# Retrieves the next item from an iterator.

my_list = [1, 2, 3]
it = iter(my_list)
print(next(it))  # Output: 1
print(next(it))  # Output: 2
print(next(it))  # Output: 3

# ord()
# =====
# Returns the Unicode code point for a one-character string.

print(ord('a'))  # Output: 97
print(ord('€'))  # Output: 8364

# pow()
# =====
# Returns the value of x to the power of y.

print(pow(2, 3))  # Output: 8
print(pow(2, 3, 5))  # Output: 3 (2^3 % 5)

# print()
# =======
# Prints the values to a stream, or to sys.stdout by default.

print('Hello, World!')  # Output: Hello, World!

# range()
# =======
# Returns an immutable sequence of numbers from start to stop by step.

print(list(range(5)))  # Output: [0, 1, 2, 3, 4]
print(list(range(1, 10, 2)))  # Output: [1, 3, 5, 7, 9]

# reversed()
# ==========
# Returns a reversed iterator.

print(list(reversed([1, 2, 3])))  # Output: [3, 2, 1]

# round()
# =======
# Rounds a number to a given precision in decimal digits.

print(round(3.14159, 2))  # Output: 3.14

# set()
# =====
# Returns a new set object, optionally with elements taken from iterable.

print(set([1, 2, 2, 3]))  # Output: {1, 2, 3}

# slice()
# =======
# Returns a slice object representing the set of indices specified by
# range(start, stop, step).

s = slice(1, 5, 2)
print(s)  # Output: slice(1, 5, 2)

# sorted()
# ========
# Returns a new sorted list from the items in iterable.

print(sorted([3, 1, 2]))  # Output: [1, 2, 3]
print(sorted('cba'))  # Output: ['a', 'b', 'c']

# str()
# =====
# Returns a str version of object.

print(str(123))  # Output: '123'
print(str(3.14))  # Output: '3.14'

# sum()
# =====
# Sums the items of an iterable from left to right and returns the total.

print(sum([1, 2, 3]))  # Output: 6
print(sum([1, 2, 3], 10))  # Output: 16

# tuple()
# =======
# Returns a tuple.

print(tuple([1, 2, 3]))  # Output: (1, 2, 3)
print(tuple('abc'))  # Output: ('a', 'b', 'c')

# type()
# ======
# Returns the type of an object or creates a new type object.

print(type(123))  # Output: <class 'int'>
print(type('abc'))  # Output: <class 'str'>

# zip()
# =====
# Returns an iterator of tuples, where the i-th tuple contains the i-th element
# from each of the argument sequences or iterables.

a = [1, 2, 3]
b = ['a', 'b', 'c']
print(list(zip(a, b)))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]