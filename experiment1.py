# Experiment 1
# Data Types, Type Conversion and Bitwise Operations

print("PYTHON DATA TYPES")
print("-----------------")

# Integer
a = 10
print("Integer:", a, type(a))

# Float
b = 10.5
print("Float:", b, type(b))

# String
c = "Python"
print("String:", c, type(c))

# Boolean
d = True
print("Boolean:", d, type(d))

# List
e = [1, 2, 3]
print("List:", e, type(e))

# Tuple
f = (1, 2, 3)
print("Tuple:", f, type(f))

# Dictionary
g = {"name": "Python", "version": 3}
print("Dictionary:", g, type(g))


print("\nTYPE CONVERSION")
print("---------------")

x = "25"
y = int(x)
print("String to Integer:", y, type(y))

x = 25
y = float(x)
print("Integer to Float:", y, type(y))

x = 25
y = str(x)
print("Integer to String:", y, type(y))


print("\nBITWISE OPERATIONS")
print("------------------")

a = 10
b = 4

print("a =", a)
print("b =", b)

print("AND  :", a & b)
print("OR   :", a | b)
print("XOR  :", a ^ b)
print("NOT  :", ~a)
print("Left Shift :", a << 1)
print("Right Shift:", a >> 1)
