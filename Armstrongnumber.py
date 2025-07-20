num = int(input("Enter the number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp%10
    sum += digit**3
    temp //= 10
if num == sum :
    print(num,"Is an arm strong number")
else:
    print("Is not armstrong number")