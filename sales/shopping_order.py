'''
    File name: shopping_order.py
    Author: Gytenis Borusas
    Date created: 12/10/2016
    Date last modified: 12/10/2016
    Python Version: 3.5

    Edited shopping list program according to pluralsight.com Object
    oriented programming lesson. Split into 3 files which are
    "shopping2.py", "shopping_cart.py", and "shopping_order.py".
'''

class Order:

    def __init__(self):
        self.quit = False
        self.add = False
        self.delete = False
        self.item = None

    def get_input(self):
        print("[command] [item] (command is to add, d to delete, "
              "q to quit) ")
        line = input()

        command = line[:1]
        self.item = line[2:]

        if command == "a":
            self.add = True
        elif command == "d":
            self.delete = True
        elif command == "q":
            self.quit = True