# Write a Python program to ask the user for two numbers and show their binary form and all bitwise results.

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print("a & b: ", a & b)
print("a | b: ", a | b)
print("a ^ b: ", a ^ b)
print("~a: ", ~a)
print("~b: ", ~b)
print("a >> b: ", a >> b)
print("a << b: ", a << b)
