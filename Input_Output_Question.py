'''
Write a python program to take marks from the user to check whether user is able to get admission in the college or not.
If marks is less than 60 then it does not allow to take admission.
Inform how many more marks is needed to be eligible, if the user is ineligible.
'''

user_name = input ("Hi, please enter your full name: ")
print ("Thank you", user_name)
marks = int(input("Please enter your total marks: "))
if marks < 60:
    print("Sorry! You are not eligible for admission. You need another", 60 - marks, "marks to be eligible.")
else:
    print("Congratulations! You are eligible for admission.")
