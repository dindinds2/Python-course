Number = int(input("Enter the number: "))
t = Number
numLen = 0
while t > 0:
    numLen = numLen+1
    t = int(t/10)
if numLen >= 4:
    numLen = int(numLen / 2)
    chk = 0
    while Number > 0:
        rem = Number % 10
        if chk == numLen:
            mid1 = rem
        elif chk == (numLen - 1):
            mid2 = rem
        Number = int(Number / 10)
        chk = chk+1
    prod = mid1 * mid2
    print("Prodect of mid digit ("+str(mid1)+"*"+str(mid2)+")=",prod)
else:
    print("Invild input")
