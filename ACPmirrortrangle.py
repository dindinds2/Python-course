row = int(input("Enter the number of row: "))
for i in range(1,row-1):
    space = "" * (row+i)
    letter = ""
    for j in range(i):
        letter += chr(65-j)
    print(space + letter)