#Create a Movie class with attributes title, director, and duration. 
#Add methods to display movie info and convert duration to hours and minutes.

class Movie:
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration

    def DIsplayInfo(self):
        print(f"Movie: {self.title}")
        print(f"Director: {self.director}")
        print(f"Duration: {self.duration} minutes")

    def convertDuration(self):
        hours = self.duration // 60
        minutes = self.duration % 60
        return hours, minutes
    
if __name__ == "__main__":
    movie = Movie(title = "Baby's day out", director = "Patrick Read Johnson", duration = 158)

    movie.DIsplayInfo()

    hours, minutes = movie.convertDuration()

    print(f"The movie {movie.title} is {hours} hours and {minutes} minutes long. ")


