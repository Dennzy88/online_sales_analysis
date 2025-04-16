# Napraviti klasu Cart koja:

# Sadrzi listu proizvoda koje korisnik doda u korpu

# Metode:

# Dodavanje proizvoda u korpu

# Prikaz sadrzaja korpe

# Racunanje ukupne vrednosti za naplatu

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)
        print(f"Added '{product.name}' to cart.")

    def view_cart(self):
        if not self.cart_items:
            print("Your cart is empty.")
        else:
            print("Cart contents:")
            for item in self.cart_items:
                item.display_info()

    def total_cart_value(self):
        total = sum(item.price * item.quantity for item in self.cart_items)
        print(f"Total cart value: ${total:.2f}")
        return total
