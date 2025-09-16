# Write a python program to generate numbers from 50 to 1, only odd numbers and find their sum

sum = 0

for i in range(50, 0, -1):
    if i % 2 == 0:
        continue
    print(i)
    sum += i

print("------------------")
print(f"Sum: {sum}")