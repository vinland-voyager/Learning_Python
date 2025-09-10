# Write a program to check whether a triangle is right angled triangle or not using pythagorus theorem

a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

if a > b and a > c:
    hypot = a;
    side1 = b;
    side2 = c;

elif b > a and b > c:
    hypot = b;
    side1 = a;
    side2 = c;

else:
    hypot = c;
    side1 = b;
    side2 = a;

if hypot**2 == side1**2 + side2**2:
    print("This triangle is right-angled.")
else:
    print("This triangle is not right-angled.")