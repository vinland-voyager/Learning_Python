# Practical 3: Write a Python program that helps students manage
# their marks, attendance, and rewards
# by calculating results and checking eligibility for extra benefits.

'''
1. Student Name
2. Student's total attendance
If eligible (i.e., >75%):
3. Student's total marks
4. Calculate results
5. Check eligibility for rewards:
- Attendance >95%:
-- Marks >95%: 5% attendance benefit in the next semester, Dean's Certificate for Excellence and 500rs cash prize
-- Marks >90%: Dean's certificate for Excellence and 500rs cash prize
-- Marks >85%: Dean's certificate for Excellence
- Attendance >90%:
-- Marks >95%: Dean's Certificate for Excellence and 500rs cash prize
-- Marks >90%: Dean's certificate for Excellence
- Attendance >85%:
-- Marks >95%: Dean's Certificate for Excellence
'''

s_name = input("Please enter your name: ")
s_attendance = int(input("Please enter your total attendance: "))
if s_attendance >= 75:
    s_marks = int(input("Please enter your total marks: "))
else:
    print("You're not eligible for examinations, let alone rewards.")

if s_attendance >= 95:
    if s_marks >= 95:
        print("Congratulations! You will receive:\n1. 5% attendance relaxation in the next semester.\n2.Dean's Certificate for Excellence.\n3. Rs. 500 Cash Prize.\n")
    elif s_marks >= 90:
        print("Congratulations! You will receive:\n1.Dean's Certificate for Excellence.\n2. Rs. 500 Cash Prize.\n")
    elif s_marks >= 85:
        print("Congratulations! You will receive Dean's Certificate for Excellence.\n")
    else:
        print("Sorry, you are not eligible for any rewards. Better luck next semester.")
elif s_attendance >= 90:
    if s_marks >= 95:
        print("Congratulations! You will receive:\n1.Dean's Certificate for Excellence.\n2. Rs. 500 Cash Prize.\n")
    elif s_marks >= 90:
        print("Congratulations! You will receive Dean's Certificate for Excellence.\n")
    else:
        print("Sorry, you are not eligible for any rewards. Better luck next semester.")
elif s_attendance >= 85:
    if s_marks >= 95:
        print("Congratulations! You will receive Dean's Certificate for Excellence.\n")
    else:
        print("Sorry, you are not eligible for any rewards. Better luck next semester.")
else:
    print("Sorry, you are not eligible for any rewards. Better luck next semester.")