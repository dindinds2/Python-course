class BMW():
    def full_speed(self):
        print("191 mph")
    def fuel_type(self):
        print("premium gasoline")

class lambo():
    def full_speed(self):
        print("340 mph")
    def fuel_type(self):
        print("Gasoline")

lambo = lambo()
bmw = BMW()
for car in (lambo,bmw):
    car.fuel_type()
    car.full_speed()