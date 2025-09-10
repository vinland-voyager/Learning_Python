# Write a Python program to extract and display the hundreds, tens, and ones digits of a given three-digit number

num = int(input("Please enter a 3-digit number: "))
while num >= 1000 or num < 100:
    print ("Please enter a three digit number.")
    num = int(input("Please enter a 3-digit number: "))

