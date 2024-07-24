# __import__()

# This function is invoked by the import statement. It can be replaced in the __builtins__ module.

math = __import__('math')
print(math.sqrt(4))  # Output: 2.0