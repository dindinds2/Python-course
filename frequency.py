dict = {'a':12,'b':12,'c':12,'d':12,'e':12,'f':23,'g':23,'h':1,'i':1,'j':1}
k = 12
res = 0
for key in dict:
    if dict[key] == k:
        res = res+1
print("frequency of k"+str(res))