num = []
enter = int(input("Enter the odd number: "))
enter1 = int(input("Enter the another odd number: "))
enter2 = int(input("Enter the another odd number: "))
enter3 = int(input("Enter the another odd number: "))
num.append(enter)
num.append(enter1)
num.append(enter2)
num.append(enter3)
num2 = [9,7,5,3,11]
odd = [i for i in num if i%2 == 0 ]
print(odd)

fruit = ["banana","apple","mango"]
print(fruit)
fruit = [item.upper() for item in fruit]
print(fruit)