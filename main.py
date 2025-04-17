# 3.Kreirati Python datoteku main.py i u njoj:

# Kreirati instancu ProductManager;
# Dodati nekoliko proizvoljnih proizvoda;
# Prikazati proizvode i ukupnu vrednost inventara.

from src.product import Product
from src.product_manager import ProductManager
from src.cart import Cart

# Kreiramo upravljaca proizvodima
manager = ProductManager()

# Dodajemo proizvode
manager.add_product(Product("Laptop", 899.99, 2))
manager.add_product(Product("Headphones", 49.99, 5))
manager.add_product(Product("Mouse", 25.50, 3))


print("\nAll Available Products:")
manager.display_all_products()


manager.total_inventory_value()

# Brisanje jednog proizvoda
print("\nRemoving 'Headphones' from inventory:")
manager.remove_product_by_name("Headphones")

# Prikaz proizvoda nakon uklanjanja
print("\nUpdated Product List:")
manager.display_all_products()



cart = Cart()


# Pronađi proizvode po imenu
for product in manager.products:
    if product.name == "Laptop" or product.name == "Mouse":
        cart.add_to_cart(product)

# Dodajmo jos jedan proizvod u korpu (simulacija nove funkcionalnosti)
cart.add_to_cart(Product("Keyboard", 59.99, 1))



print("\nYour Shopping Cart:")
cart.view_cart()

# Ukupna vrednost za naplatu
cart.total_cart_value()
