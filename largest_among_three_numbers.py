# Write a Python program to find the largest element among three numbers.

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

if (num1 > num2):
    if (num1 > num3):
        print(num1)
    elif (num1 < num3):
        print(num3)
    else:
        print(num1, num3)
elif (num1 < num2):
    if (num2 > num3):
        print(num2)
    elif (num2 < num3):
        print(num3)
    else:
        print(num2, num3)
else:
    print(num1, num2)
