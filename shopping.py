'''
    File name: shopping.py
    Author: Gytenis Borusas
    Date created: 12/10/2016
    Date last modified: 12/10/2016
    Python Version: 3.5
    A shopping list.
'''


def get_order():         #First function called by go_shopping.
    # Prints initial statement to the screen and divides the order
    # into two variables - "command" and "item".
    print("[command] [item] (command is to add, d to delete, "
          "q to quit) ")
    line = input()
    command = line[:1]
    item = line[2:]
    return command, item

def add_to_cart(item, cart):        #defines how we deal with items
    # which we already have in the list.
    if not item in cart:
        cart[item] = 0
    cart[item] += 1

def delete_from_cart(item, cart):       #defines how we deal with items
    # which we already have in the list.
    if item in cart:
        cart[item] -= 1

def process_order(order, cart):     #It's the second function called
    # from the go_shopping which defines how we deal with the inputs
    # and call two more functions to deal with those inputs.
    command, item = order
    if command == "a":
        add_to_cart(item,cart)
    elif command == "d" and item in cart:
        delete_from_cart(item, cart)
    elif command == "q":
        return False
    return True


def go_shopping():      # Main function. Initializes "cart" dictionry
    # list which is what we care about and what we will print to screen.
    # And gives the "while" loop to check if the input is valid.
    cart = dict()
    while True:
        order = get_order()
        if not process_order(order, cart):
            break

    print(cart)
    print("Finished!")

go_shopping()