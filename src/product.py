# Faza 2: Analiza podataka – Python funkcionalnosti

# 1.Kreirati Python datoteku product.py i implementirati sledeće zahteve.

# Klasa Product
# Sadrži atribute: name, price i quantity.
# Metod za prikaz informacija o proizvodu.
# Metod za ažuriranje količine proizvoda.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product: {self.name} | Price: ${self.price:.2f} | Quantity: {self.quantity}")
        
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        print(f"Quantity for '{self.name}' updated to {self.quantity}")