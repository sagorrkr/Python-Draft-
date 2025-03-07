#Create a Library class with attributes name and books. 
#Add methods add a book, remove a book, and display the total number of books.


class Library:
    def __init__(self, name):
        self.name = name
        self.books = [ ]

    def addBook(self, bookName):
        self.books.append(bookName)
        print(f"{bookName} is succesfully added to the library")

    def removeBook(self, bookName):
        if bookName in self.books:
            self.books.remove(bookName)
            print(f"{bookName} is removed from library")
        else: 
            print(f"{bookName} is not found in the library. Check again")
        
    def displayDetails(self):
        print("\nHeres the details: ")
        print(f"Number of books in {self.name}: {len(self.books)}")
        for book in self.books:
            print(book)

if __name__ == "__main__":
    library = Library(
        name = "Harry Potter library"
    )
    library.addBook("42 laws")
    library.addBook("Hanyu 2")
    library.addBook("Eat that frog")
    library.addBook("Atomic Habit")
    library.displayDetails()
    library.removeBook("Hanyu 2")
    library.displayDetails()