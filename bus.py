class vechical:
    def __init__(self,capacity,fare):
        self.capacity = capacity
        self.fare = fare
    def totalfare(self):
        return self.capacity*self.fare

class bus(vechical):
    def totalfare(self):
        basefare = super().totalfare()
        return basefare+(0.10*basefare)
    

v1 = vechical(5,100)
print("vehical total fare",v1.totalfare())
bus1 = bus(40,50)
print("Bus total fare",bus1.totalfare())