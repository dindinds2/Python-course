print("Half pyramid triangle")
num = int(input("Enter the number of row: "))
for i in range(num):
    for j in range(i+1):
        print("*",end = "")
    print()