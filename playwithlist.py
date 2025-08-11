l = [1,2,3,4,5,6]
print("Orginal list",l)
count = 0
for i in l:
    count += i
averge = count / len(l)
print("sum",count)
print("A average ", averge)
l.sort()
print("Smallest element is",l[0])
print("Largest element is",l[-1])
