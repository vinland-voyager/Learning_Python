# Write a Python program to check if the number is positive, negative, or zero.

num = int(input("Enter the number: "))

if num < 0:
    print("The number is negative.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is positive.")