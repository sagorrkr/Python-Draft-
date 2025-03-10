#Create a ShoppingCart class with attributes cart_id and items. 
#Add methods to add an item, remove an item, and calculate the total cost.

class ShoppingCart:
    def __init__(self, cart_id):
        self.cart_id = cart_id
        self.items = []

    def AddItems(self, item_name, price):
        self.items.append((item_name, price))
        print(f"Added '{item_name}' (${price:.2f}) to the cart. ")

    def RemoveItem(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                print(f"{item} removed from the cart. ")
                return
        print(f"{item_name} is not found in the cart. ")

    def calculateTotalcost(self):
        totalcost = sum(item[1] for item in self.items)
        return totalcost
    
    def displayDetails(self):
        if self.items:
            print(f"Items in the cart {self.cart_id}")
            for item in self.items:
                print(f"-{item[0]} : {item[1]: .2f}")
            print(f"Total Cost: {self.calculateTotalcost(): .2f}")
        else:
            print(f"Cart {self.cart_id}")
    
def createShopingCart():
    print("\nEnter Shopping Details: ")
    cart_id = input("Enter cart id: ")
    cart = ShoppingCart(cart_id)

    while True:
        item_name = input("Enter item name(or Done to finish)")
        if item_name.lower() == "done":
            break
        try:
            price = float(input(f"Enter the price for {item_name} $:"))
            cart.AddItems(item_name,price)
        except ValueError:
            print("Error: Invalid price.")
    return cart

if __name__ == "__main__":
    cart = createShopingCart()

    cart.displayDetails()
    cart.RemoveItem("Banana")

    removeitem = input("Enter the name of the item to remove: ")

    cart.RemoveItem(removeitem)
    cart.displayDetails()