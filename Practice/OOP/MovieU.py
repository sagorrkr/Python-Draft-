#Create a Movie class with attributes title, director, and duration. 
#Add methods to display movie info and convert duration to hours and minutes.

class Movie:
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration

    def DIsplayInfo(self):
        print(f"\nMovie: {self.title}")
        print(f"Director: {self.director}")
        print(f"Duration: {self.duration} minutes")

    def convertDuration(self):
        hours = self.duration // 60
        minutes = self.duration % 60
        return hours, minutes
    
    def displayduration(self):
        hours, minutes = self.convertDuration()
        print(f"Duration(in hours and minutes format): {hours} Hours and {minutes} minutes")
        

def createMovie():
    print(f"Enter the movie details: ")
    name = input("Movie: ")
    director = input("Director: ")
    duration = int(input("Duration(in minutes)"))
    return Movie(name, director, duration)
    
if __name__ == "__main__":
    movie = createMovie()

    movie.DIsplayInfo()

    movie.displayduration()


