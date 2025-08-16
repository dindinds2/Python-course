set = []
num = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
set.append(num**2)
set.append(num2**2)
if num%2 == 0 and num2%2 == 0:
    print("The both number is Even")
else:
    print("The both number is odd")
print(set)