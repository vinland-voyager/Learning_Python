# Write a Python program to get a name from the user and display it.
# The name should contain 5 characters or fewer than 10,
# and the name should start with the "a" character

while True:
    strvar = input("Enter your name: ")
    if len(strvar) == 5 or len(strvar) < 10:
        if strvar[0] == "a" or "A":
            break
    print ("Please enter a name starting with a and the length should be 5 or less than 10")
