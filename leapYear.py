# Write a Python program to check a year, whether it is a leap year or not

# every 4th year is leap year except 100th year but 400th year is leap year

year = int(input("Enter the year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year.")
        else:
            print("It is not a leap year.")
    else:
        print("It is a leap year.")
else:
    print("It is not a leap year.")
