# Personal notes
"""
This learning exercise helped evolve your knowledge of dictionaries.

A dictionary in Python is a data structure that associates hashable
keys to values.

Keys must be hashable and unique across the dictionary.

Key types can include numbers, strings '" or tuples () (immutable value).

Keys cannot contain mutable data structures such as lists[], dictionaries
or sets {}.

As of Python 3.7, dictionary keys are guaranteed to be the order in which
entries are inserted.

Values can be of any data type or structure.

Values can also nest arbitrarily, so they can incluse lists-of-lists, sub-
dictionaries, etc...

Compared to searching for a value within a list or array (without knowing
the index position), a dictionary uses significantly more memory, but has
very rapid retrieval.

Dictionaries are especially useful in scenarios where the collection of
items is large and must be accessed and updated frequently.

Dictionaries can be created using the dict() constructor.
>>> wombat = dict([('name', 'Wombat'), ('speed', 23), ('land_animal', True)])
{'name': 'Wombat', 'speed': 23, 'land_animal': True}
>>> whale = {'name': 'Blue Whale', 'speed': 35, 'land_animal': False}
{'name': 'Blue Whale', 'speed': 35, 'land_animal': False}

You can use [<key>] to access values in dictionaries.
>>> whale['speed']
35
>>> whale['weight']
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
KeyError: 'weight'

To avoid errors, you can use
>>> whale.get('weight', 'not found')
'not found'

You can change the values in a dictionary assigning to its keys.
>>> whale['speed'] = 25
>>> whale['speed']
25
This also functions to add new 'key: value' pairs to the dictionary.
>>> whale['weight'] = 600
>>> whale
{'name': 'Blue Whale', 'speed': 35, 'land_animal': False, 'weight': 600}

You can use the .pop(<key>) method to delete a dictionary entry. It returns
the value for use.
>>> whale.pop('weight')
600
Like .get(), you can use default values to prevent KeyErrors from being raised.
>>> whale.pop('weight', 'not found')
'not found'

You can loop through a dictionary using `for` and `while`.
>>> for key in whale:
...     print(key, whale[key])
name Blue Whale
speed 25
land_animal False
>>> for key in whale:
...     print((key, whale[key]))
('name', 'Blue Whale')
('speed', 25)
('land_animal', False)

You can also loop through a dictionary using .items(), which returns
(<key>, <value>) tuples automatically.
>>> for key, value in whale.items():
...     print(key, ':', value)
name : Blue Whale
speed : 25
land_animal : False

Likewise, .keys() method returns the keys and .values() returns the values.
>>> whale.keys()
dict_keys(['name', 'speed', 'land_animal'])
>>> whale.values()
dict_values(['Blue Whale', 25, False])
"""

# Instructions
"""
In this exercise you will be managing an inventory system.

The inventory should be organized by the item name and it should keep track of the
number of items available.

You will have to handle adding items to an inventory.

Each time an item appears in a given list, the item's quantity should be increased by
1 in the inventory. You will also have to handle deleting items from an inventory by
decreasing quantities by 1 when requested.

Finally, you will need to implement a function that will return all the key-value pairs
in a given inventory as a list of tuples.
"""

# 1. Create an inventory base on a list
"""
Implement the create_inventory(<input list>) function that creates an "inventory" from
an input list of items.

It should return a `dictionary` containing each item name paired with their respective
quantity.
"""


def create_inventory(item_list):
    inventory = dict()
    for item in item_list:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

    # Working explanation
    """
    The line
            inventory[item] = inventory.get(item, 0) + 1
    is functionaly equivalent to
            if item in inventory:
                inventory[item] += 1
            else:
                inventory[item] = 1
    , but it's more concise.
    """


# 2. Add items from a list to an existing dictionary
"""
Implement the add_items(<inventory dict>, <item list>) function that adds
a list of items to the passed-in inventory.
"""


def add_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


# 3. Decrement items from an inventory
"""
Implement the decrement_items(<inventory dict>, <items list>) function
that takes a `list` of items.

Your function should remove `1` from an item for each time that item
appears on the `list`.
"""


def decrement_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] -= 1
    return inventory

    # Working explanation
    """
    The line
            inventory[item] = inventory.get(item, 1) - 1
    is ALMOST functionaly equivalent to
            if item in inventory:
                inventory[item] -= 1
    , but it can add a new key to a passed-in dictionary.

    For example,
    >>> inventory = {'apple': 2}
    >>> items = ['apple', 'banana']
    >>> decrement_items(inventory, items)
    {'apple': 1, 'banana': 0}   # < 'banana' didn't exist before
    """


# 4. Remove an entry entirely from the inventory
"""
Implement the function remove_item(<inventory dict>, <item>) that removes
an item and its count entirely from an inventory.
"""


def remove_item(inventory, item):
    inventory.pop(item)
    return inventory


# 5. Return the entire content of the inventory
"""
Implement the list_inventory(<inventory dict>) function that takes an inventory
an returns a list of (item, quantity) tuples.

The list should only include the available items (with a quantity greater than zero).
"""


def list_inventory(inventory):
    return list(inventory.items())
