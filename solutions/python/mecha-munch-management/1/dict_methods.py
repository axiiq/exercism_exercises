"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """
    for item in set(items_to_add):
        if item in current_cart.keys():
            current_cart[item] += items_to_add.count(item)
        else:
            current_cart[item] = items_to_add.count(item)

    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """

    shopping_cart = {}
    for note in set(notes):
        shopping_cart[note] = notes.count(note)
        
    return shopping_cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """

    for recipe in recipe_updates:
        ideas[recipe[0]] = recipe[1]

    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    Parameters:
        cart (dict): A users shopping cart dictionary.

    Returns:
        dict: A sers shopping cart sorted in alphabetical order.
    """

    items = sorted(cart.keys())
    sorted_cart = {}

    for item in items:
        sorted_cart[item] = cart.get(item)
    
    return sorted_cart


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    Parameters:
        cart (dict): The users shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """

    items = sorted(cart.keys(), reverse=True)

    store_dict = {}
    for item in items:
        store_dict[item] = [cart.get(item), aisle_mapping.get(item)[0], aisle_mapping.get(item)[1]]
    
    return store_dict


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """

    for item in fulfillment_cart:
        store_inventory[item][0] -= fulfillment_cart[item][0]
        if store_inventory[item][0] <= 0:
            store_inventory[item][0] = 'Out of Stock'

    return store_inventory
