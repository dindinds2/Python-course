a = 10
b = 20
c = 30
averge = (a+b+c)/3
print(averge)
if averge > a and averge > b and averge > c :
    print("%d is higher than %d,%d,%d" % (averge,a,b,c))
elif averge > a and averge > b :
    print("%d is higher than %d,%d" % (averge,a,b))
elif averge >a and averge > c:
    print("%d is higher than %d,%d" % (averge,a,c))
elif averge >b  and averge >c:
    print("%d is higher than %d,%d" % (averge,b,c))
elif averge >a :
    print("%d is higher than %d" % (averge,a))
elif averge >b :
    print("%d is higher than %d" % (averge,b))
elif averge >c :
    print("%d is higher than %d" % (averge,c))
else:
    print("Invild input")