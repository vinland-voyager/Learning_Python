# Write a Python program to get a number from user to check, it is divisible by 2 and 3.

numVar = int(input("Enter the number: "))
if numVar % 2 == 0:
    if numVar % 3 == 0:
        print("The number is divisible by 2 & 3")
    else:
        print("The number is divisible by only 2")
else:
    print("The number is not divisible by 2 or 3.")

