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


class Airline:
    def __init__(self):
        self.flights = []
    
    def add_flight(self, flight):
        self.flights.append(flight)
        print(f"Added flight: {flight.flight_number}")