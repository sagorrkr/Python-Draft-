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
