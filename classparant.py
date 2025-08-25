class parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age

lilly = parrot("lilly",20)
deisy = parrot("deisy",21)
print("lilly is a {}".format(lilly.species))
print("deisy is a {}".format(deisy.species))
print("{} is {} years old".format(lilly.name,lilly.age))
print("{} is {} years old".format(deisy.name,deisy.age))