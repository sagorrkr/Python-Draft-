class Flight:
    def __init__(self,flight_number, origin, destination, total_seats):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.total_seats = total_seats
        self.available_seats = total_seats
    def __str__(self):
        return(f"Flight {self.flight_number} : {self.origin} to {self.destination}|"
            f"Available Seat: {self.available_seats}/{self.total_seats}")
