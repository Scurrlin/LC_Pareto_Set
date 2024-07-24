# zip()

# Returns an iterator of tuples, where the i-th tuple contains the i-th element
# from each of the argument sequences or iterables.

a = [1, 2, 3]
b = ['a', 'b', 'c']
print(list(zip(a, b)))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]