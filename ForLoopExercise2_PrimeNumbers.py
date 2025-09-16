# Write a python program to display all prime numbers within an interval

startN = int(input("Please enter the starting number: "))
endN = int(input("Please enter the ending number: "))

if startN > endN or startN == endN:
    print("The range is invalid.")

if startN < 2:
    for i in range(2, endN+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
else:
    for i in range(startN, endN+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)