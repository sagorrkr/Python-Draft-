#Write an Inventory class with attributes store_name and stock. 
#Add methods to restock, sell, and check stock level.

class Inventory:
  def __init__(self, store_name):
    self.store_name = store_name
    self.stock = 0

  def restock(self, quantity):
    if quantity > 0:
        self.stock += quantity
        print(f"Restocked {quantity} items. Current Stock: {self.stock} items")
    else:
      print("Stock quantity must be greater than 0. ")

  def sell(self, quantity):
    if quantity >= 0:    
        if quantity <= self.stock:
            self.stock -= quantity
            print(f"Sold {quantity} items. Current Stock:{self.stock} items")
        else:
           print(f" Can't sell that much. The store only has {self.stock} items. ")
    else:
       print(f"Selling quantity must be greater than 0. ")
  
  def chekStock(self):
    print(f"The current stock of the store {self.store_name} is {self.stock} items")

def createstore():
  store_name = input("Store name: ")
  return Inventory(store_name)


if __name__ == "__main__":
  store = createstore()

  store.restock(50)
  store.chekStock()

  store.sell(20)
  store.chekStock()