height = int(input("Enter the height: "))
weight = int(input("Enter the weight: "))
BMI = weight/(height/100)**2
print(BMI)
if BMI <= 19 :
    print("You are under weight")
elif BMI <= 25:
    print("You are healthly")
elif BMI <= 30:
    print("You are overweight")
else:
    print("You are obese")