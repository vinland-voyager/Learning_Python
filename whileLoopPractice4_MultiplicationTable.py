# Prompt the user to enter a number. Use a while loop to print the multiplication table of the entered number from 1 to 10

num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{num} * {i} :",num*i)
    i += 1
