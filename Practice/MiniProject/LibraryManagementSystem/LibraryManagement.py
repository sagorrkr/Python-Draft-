class Book:
    def __init__(self, title, author):
        self.title = title 
        self.author = author
        self.is_available = True

    def __str__(self):
        availability = "Available" if self.is_available else "Not Available"
        print(f"{self.title} by {self.author} - {availability}")

        
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

