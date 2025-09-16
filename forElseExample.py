numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# printing numbers until <= 5

for number in numbers:
    print(number)
    if number > 4:
        break
else:
    print("No numbers left to print.")
