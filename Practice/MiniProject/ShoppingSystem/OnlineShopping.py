class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock  = stock

    def __str__(self):
        return f"{self.name} (Id: {self.product_id}) | - {self.price:.2f} (Stock: {self.stock})"
    
    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        else:
            return False
        
class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.cari = ()
        self.order_history = []

    def __str__(self):
        return f"Customer {self.customer_id}: {self.name} , {self.email}"
    