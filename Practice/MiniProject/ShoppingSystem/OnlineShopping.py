class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock  = stock

    def __str__(self):
        return f"{self.name} (Id: {self.product_id}) | - {self.price:.2f} (Stock: {self.stock})"
    