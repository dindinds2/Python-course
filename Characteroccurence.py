name = input("Enter your name: ")
alphabet = input("Enter the alphabet")
i = 0
count = 0
while(i<len(name)):
    if (name[i] == alphabet):
        count = count+1
    i = i+1
print("The total number of time",alphabet,"Has occured",count)   
