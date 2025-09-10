# Get starting and ending numbers from user to generate a sequence of number.
# You should check at first, starting number should be less than ending number

fnum = int(input("Enter the starting number: "))
lnum = int(input("Enter the ending number: "))

if fnum > lnum:
    print("The starting number is greater. Nothing to do here.")
else:
    while fnum <= lnum:
        print(fnum)
        fnum += 1
