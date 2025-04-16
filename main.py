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


cart = Cart()


cart.add_to_cart(manager.products[0])  # Laptop
cart.add_to_cart(manager.products[2])  # Mouse


print("\nYour Shopping Cart:")
cart.view_cart()

# Ukupna vrednost za naplatu
cart.total_cart_value()
