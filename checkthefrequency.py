dict = {'codingal':2,'is':2,'best':2,'for':2,'coding':1}
print("The original dictonary"+str(dict))
k = 1
res = 0
for key in dict:
    if dict[key] == k:
        res = res+1
print("frequency of k is"+str(res))