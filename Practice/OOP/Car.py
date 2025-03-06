#Write a Car class with attributes make, model, and fuel_level. 
#Add methods to drive the car and refuel the car.

class Car:
    def __init__(self, make, model, fuel_level):
        self.make = make
        self.model = model 
        self.fuel_level = fuel_level

    def drive(self, distance):
        fuel_used = distance * 0.1
        if fuel_used <= self.fuel_level:
            self.fuel_level -= fuel_used
            print(f"Drove {distance} KM. Fuel left {self.fuel_level: .2f}")
        else:
            print("Not enough Fuel to drive that distance.")
    
    def refuel(self, amount):
        if amount > 0:
            self.fuel_level += amount
            if self.fuel_level > 100:
                self.fuel_level = 100
            print(f"Refueled {amount}%. Current fuel level {self.fuel_level: .2f}")

if __name__ == "__main__":
    car = Car(
        make = "Toyota",
        model = "premio",
        fuel_level = 100
    )

    car.drive(50)
    car.drive(100)
    car.refuel(30)