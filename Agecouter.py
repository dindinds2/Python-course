try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Something is wrong")
if age % 2 == 0:
    print("Your age is odd")
else:
    print("Your age is even")