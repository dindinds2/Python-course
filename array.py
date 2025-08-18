import array as arr
array_num = arr.array('i',[1,3,5,3,7,9,3])
print(array_num)
print("number of accurancy of the number 3 in the array"+str(array_num.count(3)))
array_num.reverse()
print("Reverse order of array"+str(array_num))