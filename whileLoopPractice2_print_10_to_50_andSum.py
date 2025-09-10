# Write a python program to generate numbers from 10 to 50 and add all the generated numbers. Solve this using while loop.

i = 50
sum = 0
while i >= 10:
    print(i)
    sum += i
    i -= 1

print(sum)
