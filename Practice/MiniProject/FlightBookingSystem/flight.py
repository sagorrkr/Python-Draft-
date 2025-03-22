class Flight:
    def __init__(self,flight_number, origin, destination, total_seats):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.total_seats = total_seats
        self.available_seats = total_seats
    def __str__(self):
        return(f"Flight {self.flight_number} : {self.origin} to {self.destination} | "
            f"Available Seat: {self.available_seats}/{self.total_seats}")

    def book_seat(self):
        if self.available_seats > 0:
            self.available_seats -= 1
            return True
        else:
            return False
        
    def cancel_seat(self):
        if self.available_seats < self.total_seats:
            self.available_seats -= 1
            return True
        else:
            return False

class Passenger: 
    def __init__(self, name, passenger_id):
        self.name = name
        self.passenger_id = passenger_id
        self.bookings = []

    def __str__(self):
        return(f"Passenger {self.passenger_id} : {self.name}")
    
    def add_bookings(self, flight):
        if flight.book_seat():
            self.bookings.append(flight)
            print(f"{self.name} has successfully booked the flight {flight.flight_number}")
        else:
            print(f"Can not book a seat for flight {self.flight_number}")

    def cancel_booking(self, flight):
        if flight in self.bookings:
            if flight.cancel_seat():
                self.bookings.remove(flight)
                print(f"{self.name} has cancelled the flight {flight.flight_number}")
            else:
                print(f"Can not cancel flight {flight.flight_number}")
        else:
            print(f"{self.name} does not have a flight for {flight.flight_number}")

    def display_bookings(self):
        if self.bookings:
            print(f"{self.name}'s Bookings: ")
            for flight in self.bookings:
                print(flight)
        else:
            print(f"No flight is booked for {self.name}")


class Airline:
    def __init__(self):
        self.flights = []
    
    def add_flight(self, flight):
        self.flights.append(flight)
        print(f"Added flight: {flight.flight_number}")

    def remove_flights(self, flight_number):
        for flight in self.flights:
            if flight.flight_number == flight_number:
                self.flights.remove(flight)
                print(f"Removed flight {flight_number}")
                return
            else:
                print(f"Flight {flight_number} not found.")
            
    def search_flight(self, flight_number):
        for flight in self.flights:
            if flight.flight_number == flight_number:
                return flight
        return None
    
    def display_flights(self):
        if self.flights:
            print("\nAvailable Flights: ")
            for flight in self.flights:
                print(flight)
        else:
            print("\nNo flights Available. ")

#testing the code
            
if __name__ == "__main__":
    airline = Airline()

    flight1 = Flight(flight_number = "F101", origin = "Dhaka", destination = "New York", total_seats = 100)
    flight2 = Flight(flight_number = "F102", origin = "Dhaka", destination = "Beijing", total_seats = 120)
    flight3 = Flight(flight_number = "F103", origin = "Dhaka", destination = "London", total_seats = 110)


    airline.add_flight(flight1)
    airline.add_flight(flight2)
    airline.add_flight(flight3)

    airline.display_flights()

    passenger1 = Passenger(name = "Roy", passenger_id = "5203004")
    passenger2 = Passenger(name = "Bob", passenger_id = "5103005")

    passenger1.add_bookings(flight1)
    passenger2.add_bookings(flight2)

    passenger1.display_bookings()
    passenger2.display_bookings()

    passenger1.cancel_booking(flight1)
    passenger2.cancel_booking(flight1)

    passenger1.display_bookings()

    airline.display_flights()