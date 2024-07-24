# issubclass()

# Returns True if class is a subclass (direct, indirect or virtual) of
# classinfo.

class A:
    pass

class B(A):
    pass

print(issubclass(B, A))  # Output: True
print(issubclass(A, B))  # Output: False
