'''
    File name: shopping_order.py
    Author: Gytenis Borusas
    Date created: 12/10/2016
    Date last modified: 12/11/2016
    Python Version: 3.5

    Edited shopping list program according to pluralsight.com Object
    oriented programming lesson. Split into 3 files which are
    "shopping2.py", "shopping_cart.py", and "shopping_order.py".
'''

class Order:

    def __init__(self):     # Initializes all imput variables as
        # false in the beggining.
        self.quit = False
        self.add = False
        self.delete = False
        self.item = None

    def get_input(self):
        print("[command] [item] (command is to add, d to delete, "
              "q to quit) ")
        line = input()

        command = line[:1]      # Reads one line imput as two
        # separate variables.
        self.item = line[2:]         # Reads one line imput as two
        # separate variables.

        if command == "a":      # Defines what first part of command
            # means.
            self.add = True
        elif command == "d":      # Defines what first part of command
            # means.
            self.delete = True
        elif command == "q":      # Defines what first part of command
            # means.
            self.quit = True