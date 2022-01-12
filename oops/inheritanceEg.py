# Parent
class Vehicle:
    def __init__(self, make, model, fuel):
        self.make = make
        self.model = model
        self.fuel = fuel

# Child
class Car(Vehicle):
    def __init__(self, make, model, fuel, stero_system, sunroof):
        # Parent attributes
        Vehicle.make = make
        Vehicle.model = model
        Vehicle.fuel = fuel
        self.stero_system = stero_system
        self.sunroof = sunroof

    def show_parent_attribute(self):
        print(Vehicle.make," ",Vehicle.model," ",Vehicle.fuel)


myObj = Car("Tesla", 2019, 'Electrice', True, False)

print(myObj.__dict__)
print(myObj.make)
myObj.show_parent_attribute()