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
        self.cart = Cart()
        self.order_history = []

    def __str__(self):
        return f"Customer {self.customer_id}: {self.name} , {self.email}"
    
    def place_order(self):
        if self.cart.products:
            order = Order(customer = self, products = self.cart.products)
            self.order_history.append(order)
            self.cart.clear_cart()
        else:
            print("Your cart is empty. Add products to place order.")

    def view_order_history(self):
        if self.order_history:
            print(f"{self.name}'s order history: ")
            for order in self.order_history:
                print(order)
        else:
            print(f"{self.name} has no order history.")



class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product, quantity = 1):
        if product.reduce_stock(quantity):
            self.products.append((product, quantity)) 
            print(f"Added {quantity} x {product.name} to the cart.")
        else:
            print(f"Insuffecient stock for {product.name}")

    def remove_products(self, product):
        for item in self.products:
            if item[0].product_id == product.product_id:
                self.products.remove(item)
                print(f"Removed {product.name} from Cart.")
                return
        print(f"{product.name} not found in the Cart.")

    def view_cart(self):
        if self.products:
            print(f"\nYour cart:")
            total = 0
            for product, quantity in self.products:
                print(f"{product.name} x {quantity} - {product.price * quantity: .2f}")
                total += product.price * quantity
            print(f"Your total is {total: .2f}")
        else:
            print("Your cart is empty.")
    def clear_cart(self):
        self.products = []

class Order:
    order_counter = 1
    
    def __init__(self, customer, products):
        self.order_id = Order.order_counter
        Order.order_counter += 1
        self.customer = customer
        self.products = products
        self.total_price = sum(product.price * quantity for product, quantity in products)
    def __str__(self):
        order_detsils = "\n".join(f"{quantity} x {product.name} - {product.price * quantity: .2f}" for product, quantity in self.products)

        return(f"Order Id: {self.order_id} \n"
               f"Customer: {self.customer.name} \n"
               f"Products: \n{order_detsils} \n"
               f"Total: {self.total_price:.2f}")


if __name__ == "__main__":
    product1 = Product(product_id=1, name="Laptop", price=999.99, stock=10)
    product2 = Product(product_id=2, name="Mobile", price=599.99, stock=10)
    product3 = Product(product_id=3, name="Headphones", price=99.99, stock=100)

    customer = Customer(customer_id = 1122, name = "Bob", email = "bob@vscode.com")

    customer.cart.add_product(product1, quantity = 3)
    customer.cart.add_product(product2, quantity = 2)
    customer.cart.add_product(product3, quantity = 4)

    customer.cart.view_cart()
