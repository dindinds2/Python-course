lower = int(input("Enter the number: "))
upper = int(input("Enter the number: "))
print("The prime number between",lower,"and",upper,"=")
for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if(num % i) == 0:
                break
        else:
            print(num)