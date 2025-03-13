#Create a Vehicle class with attributes brand and model. Inherit it in Car and Bike classes. 
#Add unique methods for each child class.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def displayInfo(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, number_doors):
        super().__init__(brand, model)
        self.number_doors = number_doors

    def drive(self):
        print(f"Driving the {self.brand} {self.model} with {self.number_doors} doors.")

class Bike(Vehicle):
    def __init__(self, brand, model, cc):
        super().__init__(brand, model)
        self.cc = cc

    def ride(self):
        print(f"Riding the {self.cc} CC {self.brand}{self.model} bike. ")

if __name__ == "__main__":
    car = Car(brand = "Toyota", model = "Premio", number_doors = 4)

    bike = Bike(brand = "Yamaha", model = "FZS V2", cc = 160)

    car.displayInfo()
    bike.ride()
    car.drive()