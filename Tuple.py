tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

result = tuple(tup1*tup2 for tup1,tup2 in zip(tup1,tup2))
print(result)