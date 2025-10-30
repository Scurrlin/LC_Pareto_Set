# 1 - Control Flow
# ================
# if

x = 10
if x > 5:
    print("x is greater than 5")

# elif

x = 10
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is 10")

# else

x = 5
if x > 10:
    print("x is greater than 10")
else:
    print("x is 10 or less")

# for

for i in range(5):
    print(i)

# while

i = 0
while i < 5:
    print(i)
    i += 1

# break

for i in range(5):
    if i == 3:
        break
    print(i)

# continue

for i in range(5):
    if i == 3:
        continue
    print(i)

# pass

def some_function():
    pass

# 2 - Exception Handling
# ======================
# try

try:
    x = 1 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# except

try:
    x = 1 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# finally

try:
    x = 1 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("This is always executed")

# raise

def check_positive(x):
    if x < 0:
        raise ValueError("Only positive numbers are allowed")
check_positive(-1)

# assert

x = 10
assert x > 0, "x should be positive"

# 3 - Function and Class Definitions
# ==================================
# def

def greet(name):
    return f"Hello, {name}!"

# lambda

add = lambda x, y:x + y
print(add(2, 3))

# class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 4 - Variable Scope and Namespace
# ================================
# global

x = 10
def modify_global():
    global x
    x = 5
modify_global()
print(x)  # Output: 5

# nonlocal

def outer_function():
    x = "local"
    def inner_function():
        nonlocal x
        x = "nonlocal"
    inner_function()
    print(x)  # Output: nonlocal
outer_function()

# del

x = 10
del x
# print(x) would raise NameError

# 5 - Boolean and None
# ====================
# True

is_active = True
if is_active:
    print("Active")

# False

is_active = False
if not is_active:
    print("Inactive")

# None

x = None
if x is None:
    print("x is None")

# 6 - Logical Operators
# =====================
# and

x = 10
y = 5
if x > 5 and y < 10:
    print("Both conditions are True")

# or

x = 10
y = 15
if x > 5 or y < 10:
    print("At least one condition is True")

# not

is_active = False
if not is_active:
    print("Inactive")

# is

x = None
if x is None:
    print("x is None")

# in

fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list")

# 7 - Asynchronous Programming
# ============================
# async 

import asyncio

async def say_hello():
    print("Hello")

asyncio.run(say_hello())

# await

import asyncio

async def say_hello():
    await asyncio.sleep(1)
    print("Hello")

asyncio.run(say_hello())

# 8 - Context Management
# ======================
# with

with open("test.txt", "w") as file:
    file.write("Hello, world!")

# 9 - Importing Modules
# =====================
# import

import math
print(math.sqrt(16))

# from

from math import sqrt
print(sqrt(16))

# 10 - OOP
# ========
# class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# del

class Person:
    def __init__(self, name):
        self.name = name

person = Person("John")
del person.name
# Accessing person.name now would raise an AttributeError

# 11 - Miscellaneous
# ==================
# as

import math as m
print(m.sqrt(16))

# yield

def generator():
    yield 1
    yield 2
    yield 3

for value in generator():
    print(value)

# return

def add(a, b):
    return a + b
print(add(2, 3))