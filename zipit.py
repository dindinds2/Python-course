s1 = {1,2,3}
s2 = {'a','b','c'}
s3 = list(zip(s1,s2))
print(s3)
list1 = [10,20,30]
list2 = [40,50,60]
for x,y in zip(list1,list2[::-1]):
    print(x,y)
fruit = ['apple','banana','mango']
price = [100,200,300]
new_dict = {fruit:price for fruit,price in zip(fruit,price)}
print('\n{}'.format(new_dict))