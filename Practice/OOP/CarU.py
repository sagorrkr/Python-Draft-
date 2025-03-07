#Write a Car class with attributes make, model, and fuel_level. 
#Add methods to drive the car and refuel the car.
class Car:
    def __init__(self, make, model, fuel_level):
        self.make = make
        self.model = model
        self.fuel_level = fuel_level
    
    def drive(self, distance):
        fuel_used = distance * 0.1
        self.fuel_level -= fuel_used
        print(f"Drove {distance} KM. Current Fuel Level {self.fuel_level: .2f}")


    def refuel(self, amount):
        if amount > 0:
            self.fuel_level += amount
            if self.fuel_level > 100:
                self.fuel_level = 100
            print(f"Refueled {amount}%. Current Fuel Level {self.fuel_level: .2f}")
        else:
            print("Error. Can't be negative number. ")
    
    def DisplayDetails(self):
        print("\nHere is the car details:")
        print(f"Brand: {self.make}")
        print(f"Model: {self.model}")
        print(f"Fuel Level: {self.fuel_level}")


def createCar():
    print("Enter the car details:")
    make = input("Car Brand: ")
    model = input("Car Model: ")
    fuel_level = float(input("Fuel level: "))

    return Car(make, model, fuel_level)


if __name__ == "__main__":
    car = createCar()

    car.drive(200)
    car.DisplayDetails

