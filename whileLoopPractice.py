# Write a Python program to generate numbers from 100 to 1 but only for odd numbers

i = 100
while i > 0:
    if i%2 == 0:
        i -= 1
        continue
    else:
        print(i)
        i -= 1