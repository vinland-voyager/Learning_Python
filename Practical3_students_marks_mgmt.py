# Practical 3: Write a Python program that helps students manage
# their marks, attendance, and rewards
# by calculating results and checking eligibility for extra benefits.

'''
1. Student Name
2. Student's total attendance: comprises for 15% value
3. Student's total marks: comprises for 70% value
4. Student's club: comprises for 15% value
5. Calculate results
'''

s_name = input("Please enter your name: ")
s_attendance = int(input("Please enter your total attendance out of 100: "))
s_marks = int(input("Please enter your total marks out of 100: "))
clubs = ["hackfire", "dance", "music", "fashion", "poetry"]
s_club = str.lower(input("Are you in any of these clubs: Hackfire | Dance | Music | Fashion | Poetry? If so, please enter the name of your club: "))

if s_club in clubs:
    result = (s_attendance*0.15) + (s_marks*0.7) + 15
else:
    result = (s_attendance*0.15) + (s_marks*0.7)

print("Your result: ", result)

'''
# Discard:
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

Rewards:

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
'''