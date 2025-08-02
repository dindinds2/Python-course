def factorail(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorail(n-1)
num = int(input("Enter the number: "))
if num < 0:
    print("Factorial is not define for negative number")
else:
    result = factorail(num)
    print(f"The factorail of {num} is {result}")