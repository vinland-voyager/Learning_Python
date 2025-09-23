# Separate even and odd numbers into two lists

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenList = []
oddList = []

for i in lst:
    if i % 2 == 0:
        evenList.append(i)
    else:
        oddList.append(i)

print(evenList)
print(oddList)