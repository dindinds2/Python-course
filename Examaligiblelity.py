Medicalcondition = input("Do you have medical condition  Y/N")
attendance = int(input("Enter the attendance of the student: "))
if Medicalcondition == 'Y' :
    print("You are allowed")
else:
    if attendance >= 75 :
        print("You are allowed")
    else:
        print("You are not allowed")
        