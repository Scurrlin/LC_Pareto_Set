# filter()

# Constructs an iterator from elements of an iterable for which a function
# returns true.

def is_even(n):
    return n % 2 == 0

result = filter(is_even, [1, 2, 3, 4])
print(list(result))  # Output: [2, 4]
