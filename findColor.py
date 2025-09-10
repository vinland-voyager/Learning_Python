# Write a Python program to find the occurrence of a specific color from a list

colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

checkVar = str.lower(input("Please enter the color to check: "))

if checkVar in colors:
    print("Color is in the list.")
else:
    print("Color is not in the list.")