# locals()

# Returns a dictionary representing the current local symbol table.

def func():
    a = 1
    print(locals())

func()  # Output: {'a': 1}