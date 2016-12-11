'''
    File name: shopping.py
    Author: Gytenis Borusas
    Date created: 12/10/2016
    Date last modified: 12/10/2016
    Python Version: 3.5

    Edited shopping list program according to pluralsight.com Object
    oriented programming lesson. Split into 3 files which are
    "shopping2.py", "shopping_cart.py", and "shopping_order.py".
'''

import sales.shopping_cart, sales.shopping_order

cart = sales.shopping_cart.Cart()
order = sales.shopping_order.Order()
order.get_input()

while not order.quit:
    cart.process(order)
    order = sales.shopping_order.Order()
    order.get_input()

print(cart)