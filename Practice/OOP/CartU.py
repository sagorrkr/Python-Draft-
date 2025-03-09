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
    
def createShopingCart():

if __name__ == "__main__":
    cart = ShoppingCart(cart_id = "C69")

    cart.AddItems("Apple", 2.0)
    cart.AddItems("Banana", 1.5)
    cart.AddItems("Orange", 3.0)

    cart.RemoveItem("Banana")

    print(f"Total cost: {cart.calculateTotalcost(): .2f}")