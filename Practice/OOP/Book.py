#Create a Book class with attributes title, author, and price. Add a method to display the book details.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print("\nHere's the book details:")
        print(f"Name: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price }")

if __name__ == "__main__":
    
    book = Book(title = "Eat the frog", author = "Brian Tracy", price = 299)

    book.display_details()