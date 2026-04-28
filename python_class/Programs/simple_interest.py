# (c) Function with default parameters for Simple Interest
def simple_interest(p=1000, r=5, t=2):
    return (p * r * t) / 100


# (a) Accept input from user (instead of command line)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# (b) Arithmetic operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
else:
    print("Division: Not possible")

# Using default parameters
print("\nSimple Interest (default):", simple_interest())

# Using user values
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

print("Simple Interest (custom):", simple_interest(p, r, t))