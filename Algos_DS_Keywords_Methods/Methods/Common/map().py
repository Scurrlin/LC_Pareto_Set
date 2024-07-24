# map()

# Applies a function to every item of an iterable and returns a list of the results.

def square(n):
    return n * n

result = map(square, [1, 2, 3, 4])
print(list(result))  # Output: [1, 4, 9, 16]