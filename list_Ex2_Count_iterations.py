# Count how many times each element appears
# Practical 5: Write a Python program to check whether a given number is palindrome or not | Use for loop

elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
element_counts = {}
for element in elements:
    if element in element_counts:
        element_counts[element] += 1
    else:
        element_counts[element] = 1
print(element_counts)
