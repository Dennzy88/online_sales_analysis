# 2.Kreirati Python datoteku product_manager.py i implementirati sledece zahteve.

# Klasa ProductManager
# Sadrzi kao atribut listu svih dostupnih proizvoda.
# Dodavanje proizvoda.
# Prikaz svih proizvoda.
# Prikaz ukupne vrednosti svih proizvoda.

from src.product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product '{product.name}' added.")

    def display_all_products(self):
        if not self.products:
            print("No products available.")
        else:
            for product in self.products:
                product.display_info()

    def total_inventory_value(self):
        total = sum(product.price * product.quantity for product in self.products)
        print(f"Total inventory value: ${total:.2f}")
        return total

    def remove_product_by_name(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                self.products.remove(product)
                print(f"Product '{name}' removed.")
                return
        print(f"No product found with name '{name}'.")
