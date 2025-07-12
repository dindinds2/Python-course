print("Enter mark of 5 subject")
math = int(input())
english = int(input())
history = int(input())
social = int(input())
science = int(input())
total = math+english+history+social+science
average = total / 5
if average >= 91 and average<=100:
    print("Your grade is A1")
elif average >= 81 and average<91:
    print("Your grade is A2")
elif average >= 71 and average<81:
    print("Your grade is B1")
elif average >= 61 and average<71:
    print("Your grade is B2")
elif average >= 51 and average<61:
    print("Your grade is C1")
elif average >= 41 and average<51:
    print("Your grade is C2")
elif average >= 31 and average<41:
    print("Your grade is D1")
elif average >= 21 and average<31:
    print("Your grade is D2")
elif average >= 11 and average<21:
    print("Your grade is E1")
elif average >= 1 and average<11:
    print("Your grade is E2")
else:
    print("Invalid input")