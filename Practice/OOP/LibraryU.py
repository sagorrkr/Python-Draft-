#Create a Library class with attributes name and books. 
#Add methods add a book, remove a book, and display the total number of books.


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def addBook(self, book_titles):
        self.books.append(book_titles)
        print(f"{book_titles} is succesfully added to the library")

    def addBooks(self, book_titles):
        for book in book_titles:
            self.addBook(book.strip())

    def removeBook(self, bookName):
        if bookName in self.books:
            self.books.remove(bookName)
            print(f"{bookName} is removed from library")
        else: 
            print(f"{bookName} is not found in the library. Check again")
        
    def displayDetails(self):
        print("\nHere's the details: ")
        print(f"Number of books in {self.name}: {len(self.books)}")
        for book in self.books:
            print(f"-{book}")


def create_library():
    print("\nEnter Details: ")
    name = input("Library Name: ")
    library = Library(name)
    book_titles = list(map(str, input("Enter book names(separated by comma): ").split(",")))
    library.addBooks(book_titles)
    return library

    

if __name__ == "__main__":
    library = create_library()

    library.addBook("42 laws")
    library.addBook("Hanyu 2")
    library.addBook("Eat that frog")
    library.addBook("Atomic Habit")
    library.displayDetails()
    library.removeBook("Hanyu 2")
    library.displayDetails()