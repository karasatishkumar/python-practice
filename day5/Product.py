class Product:
    total = 0  # class data-member

    def __init__(self, name, qty):
        self.name = name
        self.qty = qty
        Product.total += self.qty

    def show(self):
        print(self.name, self.qty)

    @classmethod  # class method
    def display(cls):
        print("Total = ", Product.total)
        print("Total = ", cls.total)


p1 = Product("A", 10)
p2 = Product("B", 20)
p3 = Product("C", 30)
Product.display()  # p3.display()