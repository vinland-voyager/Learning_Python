#Reverse a list without using the reverse() method.

original_list = [1, 2, 3, 4, 5]
reversed_list = []
for i in range(len(original_list) - 1, -1, -1):
    reversed_list.append(original_list[i])
print(reversed_list)