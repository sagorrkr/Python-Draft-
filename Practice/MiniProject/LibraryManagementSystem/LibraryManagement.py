class Book:
    def __init__(self, title, author):
        self.title = title 
        self.author = author
        self.is_available = True

    def __str__(self):
        availability = "Available" if self.is_available else "Not Available"
        return(f"{self.title} by {self.author} - {availability}")

        
class Library:
    def __init__(self):
        self.books = []

    def add_books(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Added {title} by {author} to the Library")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Removed {title} from the Library. ")
                return
        print(f"The book {title} is not found in Library. ")
    
    def display_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        if available_books:
            print(f"\nAvailable Books: ")
            for book in available_books:
                print(book)
        else:
            print("No book is available in the library.")
    def borrow_books(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_available:
                    book.is_available = False
                    print(f"You've borrowed {title}.")
                else:
                    print(f"{title} is not available for borrowing.")
#        print(f"Book {title} is not found in the library. ")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.is_available:
                    book.is_available = True
                    print(f"You've returned the book {title}")
                else:
                    print(f"{title} is already available in the library. ")
#        print(f"Book {title} is not found in the library")

#let's test the code
if __name__ == "__main__":
    library = Library()
    library.add_books("1984","George Orwell")
    library.add_books("Atoms","George Wilder")
    library.add_books("Physics","George Fyneman")
    library.add_books("To Kill a Mockingbird", "Harper Lee")
    library.add_books("The Great Gatsby", "F. Scott Fitzgerald")

    library.display_available_books()
    library.borrow_books("1984")
    # Attempt to borrow the same book again
    library.borrow_books("1984")  

    # Display available books after borrowing
    library.display_available_books()

    # Return a book
    library.return_book("1984")
    # Attempt to return the same book again
    library.return_book("1984")  

    # Display available books after returning
    library.display_available_books()

    # Remove a book
    library.remove_book("To Kill a Mockingbird")

    # Display available books after removal
    library.display_available_books()

