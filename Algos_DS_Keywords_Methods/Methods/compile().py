# compile()

# Compiles source into a code or AST object.

code = compile('a = 5\nb = 6\nprint(a + b)', 'example', 'exec')
exec(code)  # Output: 11
