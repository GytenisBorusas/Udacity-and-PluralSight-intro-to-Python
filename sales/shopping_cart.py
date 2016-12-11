'''
    File name: shopping_cart.py
    Author: Gytenis Borusas
    Date created: 12/10/2016
    Date last modified: 12/11/2016
    Python Version: 3.5

    Edited shopping list program according to pluralsight.com Object
    oriented programming lesson. Split into 3 files which are
    "shopping2.py", "shopping_cart.py", and "shopping_order.py".
'''


class Cart:

    def __init__(self):
        self._contents = dict()

    def __repr__(self):
        return "{0} {1}".format(Cart, self.__dict__)        # Returns
        #  number 0 and number 1 values from the self.__dict__
        # dictionary

    def process(self, order):
        if order.add:
            if not order.item in self._contents:
                self._contents[order.item] = 0     # Defines initial
                # value for the pass in items.
            self._contents[order.item] += 1     # Defines what to
                # do with the item passed into the cart if it a
                # same object.
        elif order.delete:
            if order.item in self._contents:
                self._contents[order.item] -= 1     # Defines what to
                #  do with deleted items.
                if self._contents[order.item]  <= 0:
                    del self._contents[order.item]      # Checks if
                    # the deleted item is the last item of that type
                    # in the cart and deletes the name totally if it is.



