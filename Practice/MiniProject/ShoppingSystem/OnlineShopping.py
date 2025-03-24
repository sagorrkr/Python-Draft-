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
    
    def place_order(self):
        if self.cart.products:
            order = Order(customer = self, products = self.cart.products)


class Cart:
    def __init__(self):
        self.products = []

    def add_products(self, product, quantity = 1):
        if product.reduce_stock(quantity):
            self.products.append(product, quantity)
            print(f"Added {quantity} x {product.name} to the cart.")
        else:
            print(f"Insuffecient stock for {product.name}")

class Order:
    order_counter = 1
    
    def __init__(self, customer, products):
        self.order_id = Order.order.counter
        Order.order_counter += 1
        self.customer = customer
        self.products = products
        self.total_price = sum(product.price * quantity for product, quantity in products)