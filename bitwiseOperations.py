# Write a Python program to perform left and right shift bitwise operations.

num = int(input("Enter a number: "))
change = int(input("Enter number of positions to shift: "))

print("Left Shift: ", num << change)
print("Right Shift: ", num >> change)
