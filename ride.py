print("Select your ride")
print("1.Bike")
print("2.Car")
choice = int(input("Enter your choice: "))
if (choice == 1):
    print("What type of bike")
    print("1.Scooty")
    print("2.Scooter")
    choice2 = int(input("Enter your choice: "))
    if choice2 == 1:
        print("You have selected Scooty")
    else:
        print("You have selected scooter")
elif (choice == 2):
    print("What type of car")
    print("1.Sedan")
    print("2.SUV")
    choice3 = int(input("Enter your choice: "))
    if choice3 == 1:
        print("You have selected Sedan")
    else:
        print("You have selected SUV")
else:
    print("Invild input")