#Create a Book class with attributes title, author, and price. Add a method to display the book details.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print("\nBook Details: ")
        print(f"Name: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price: .2f}")

def create_book():
    print("Enter Book Details: ")
    title = input("Enter Title: ")
    author = input("Author: ")
    while True:
        try:
            price = int(input("Price: "))
            if price >= 0:
                break
            else: 
                print("Price can't be less than 0")
        except ValueError:
            print("Error: Only positive int is allowed.")
    return Book(title, author, price)
    
if __name__ == "__main__":
    book = create_book()
    book.display_details()

        
