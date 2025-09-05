class india():
    def capital(self):
        print("New Delhi is the captial of india")
    def lang(self):
        print("Hindi is the lang")
    def type(self):
        print("Is a developing country")

class usa():
    def capital(self):
        print("Washington DC is the captial of usa")
    def lang(self):
        print("english is the lang")
    def type(self):
        print("Is a develop country")

obj_ind = india()
obj_usa = usa()
for country in (obj_ind,obj_usa):
    country.capital()
    country.lang()
    country.type()
    