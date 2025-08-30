class pair_element:
    def twosum(self,num,target):
        lookup = {}
        for i,number in enumerate(num):
            if target - number in lookup:
                return(lookup[target-number],i)
            lookup[number] = i

value = int(input("Enter sum for which you want to make this search: "))
print("index1 = %d,index2 = %d"%pair_element().twosum((10,20,30,40,50,60,70),value))