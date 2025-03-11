#Write an Inventory class with attributes store_name and stock. 
#Add methods to restock, sell, and check stock level.

class Inventory:
  def __init__(self, store_name, stock):
    self.store_name = store_name
    self.stock = stock

  def restock(self, add_stock):
    self.stock += add_stock

  def sell(self, sell):
    self.stock -= sell
  
  def chcekStock(self):
    return self.stock

if __name__ == "__main__":
  store = Inventory(store_name = "ABC", stock = 100)

  store.restock(50)
  print(store.chcekStock())

  store.sell(20)
  print(store.chcekStock())
