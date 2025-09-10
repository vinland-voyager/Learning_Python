# Write a Python program to check a valid username and password.

username = "Test"
password = "<PASSWORD>"

chkUsername = input("Enter your username: ")
chkPassword = input("Enter your password: ")

if chkUsername == username and chkPassword == password:
    print("Yes, your username and password are correct.")
else:
    print("No, your username and password are incorrect.")