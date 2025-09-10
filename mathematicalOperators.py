# Write a Python program to get 4 numbers from the user,
# subtract the first two, add the second two numbers,
# then find the multiplication of both results.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

result = (num1 - num2) * (num3 + num4)

print(result)