class dog:
    def __init__(self,dog_breed,color):
        self.dog_breed = dog_breed
        self.color = color

ob = dog("German Shepherd","Black")
print(ob.dog_breed,ob.color)