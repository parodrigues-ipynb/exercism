# Personal notes
"""
This exercise helped evolve your knowledge of dictionaries.

The `dict` class in Python provides many useful methods for working with
dictionaries.

------------------------ From previous exercise ------------------------
>>> whale = {'name': 'Blue Whale', 'speed': 35, 'land_animal': False}
>>> whale['speed']
35
>>> whale['speed'] = 25
>>> whale['speed']
25
>>> whale['weight'] = 600
>>> whale
{'name': 'Blue Whale', 'speed': 35, 'land_animal': False, 'weight': 600}

>>> whale.pop('weight')
600
>>> whale.pop('weight', 'not found')
'not found'


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
>>> for key, value in whale.items():
...     print(key, ':', value)
name : Blue Whale
speed : 25
land_animal : False

>>> whale.keys()
dict_keys(['name', 'speed', 'land_animal'])
>>> whale.values()
dict_values(['Blue Whale', 25, False])
------------------------------------------------------------------------

You can use .setdefault(key, <default value>) for Error-Free insertion.
>>> palette_I = {'Grassy Green': '#9bc400',
                 'Purple Mountains Majesty': '#8076a3',
                 'Misty Mountain Pink': '#f9c5bd'}
>>> palette_I.setdefault('Rock Brown', '#694605')
'#694605'
>>> palette_I.setdefault('Purple Mountains Majesty', 'aaaa')
'#8076a3'
>>> palette_I
{'Grassy Green': '#9bc400',
'Purple Mountains Majesty': '#8076a3',
'Misty Mountain Pink': '#f9c5bd',
'Rock Brown': '#694605'}

.fromkeys() quickly populate a dictionary with various `keys` and default
values.
>>> new_dict = dict.fromkeys(['Grassy Green', 'Purple Mountains Majesty', 'Misty Mountain Pink'], 'fill in hex color here')
>>> new_dict
{'Grassy Green': 'fill in hex color here',
 'Purple Mountains Majesty': 'fill in hex color here',
 'Misty Mountain Pink': 'fill in hex color here'}

The .keys(), .values() and .items() are dynamic views.
If the value of an entry in a dictionary should change, then the views change as well.
>>> palette_I = {'Grassy Green': '#9bc400',
             'Purple Mountains Majesty': '#8076a3',
             'Misty Mountain Pink': '#f9c5bd'}
>>> palette_I.keys()
dict_keys(['Grassy Green', 'Purple Mountains Majesty', 'Misty Mountain Pink'])
>>> palette_I.values()
dict_values(['#9bc400', '#8076a3', '#f9c5bd'])
>>> palette_I.items()
dict_items([('Grassy Green', '#9bc400'), ('Purple Mountains Majesty', '#8076a3'), ('Misty Mountain Pink', '#f9c5bd')])

reversed(<dict>.keys(), .values() or .items()) reverses the order of entries in a dictionary without altering
the original dictionary.

Dictionaries do not have a built-in sorting method. However, it is possible to sort
a `dict` view using the built-in function sorted() with dict.items().
The sorted view can then be used to create a new dictionary. Like iteration, the
default sort is over the dictionary `keys`.
>>> color_palette = {'Grassy Green': '#9bc400', 
                     'Purple Mountains Majesty': '#8076a3', 
                     'Misty Mountain Pink': '#f9c5bd', 
                     'Factory Stone Purple': '#7c677f', 
                     'Green Treeline': '#478559', 
                     'Purple baseline': '#161748'}
>>> sorted_palette = dict(sorted(color_palette.items()))
>>> sorted_palette
{'Factory Stone Purple': '#7c677f',
 'Grassy Green': '#9bc400',
 'Green Treeline': '#478559',
 'Misty Mountain Pink': '#f9c5bd',
 'Purple Mountains Majesty': '#8076a3',
 'Purple baseline': '#161748'}

<dict_one>.update(<dict_two>) combines two dictionaries. Where keys overlap,
the value in dict_one will be overwritten by the corresponding value from
dict_two.

You can also use the Union Operator (|), which creates a new dictionary.
>>> dict_one | dict_two
When both dictionares share keys, dict_two values take precedence.

dict_one |= other behaves similar to <dict_one>.update(<other>), but in this
case <other> can be either a `dict` or an iterable of (key value) pairs.
"""

# Instructions
"""
Mecha Munch, a grocery shopping automation company, has just hired you to work
on their ordering app.

Your team is tasked with building an MVP (minimum viable product) that manages
all the basic shopping cart activities, allowing users to add, remove and sort
their grocery orders.

Thankfully, a different team is handling all the money and check-out functions!
"""


# 1. Add item(s) to the users shopping cart
"""
The MVP should allow the user to add items to their shopping cart.

This could be a single item or multiple items at once.

Since this is an MVP, item quantity is indicated by repeats. If a user wants to
add 2 Oranges, 'Orange' will appear twice in the input iterable.

If the user already has the item in their cart, the cart quantity should be
increased by 1. If the item is new to the cart, it should be added with a quantity
of 1.

Create the function add_item(<current_cart>, <items_to_add>) that takes a cart
dictionary and any list-like iterable of items to add as arguments. It should return
a new/updated shopping cart dictionary for the user.
"""


def add_item(current_cart, items_to_add):
    """
    Add items to shopping cart.

    Args:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): Items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.

    Examples:
    >>> add_item({'Banana': 3, 'Apple': 2, 'Orange': 1},
    ...          ('Apple', 'Apple', 'Orange', 'Apple', 'Banana'))
    {'Banana': 4, 'Apple': 5, 'Orange': 2}
    """
    for item in items_to_add:
        current_cart[item] = current_cart.setdefault(item, 0) + 1
    return current_cart


# 2. Read in items listed in the users notes app
"""
Uh-oh. Looks like the product team is engaging in feature creep. They
want to add extra functionality to the MVP.

The application now has to create a shopping cart by reading items off
a users note app. Convenient for the users, but slightly more work for
the team.

Create the function read_notes(<notes>) that can take any list-like
iterable as an argument. The function should parse the items and create
a user shopping cart/dictionary.

Each item should be added with a quantity of 1. The new user cart should
then be returned.
"""


def read_notes(notes):
    """
    Create user cart from an iterable notes entry.

    Args:
        notes (iterable): Iterable of items to add to cart.

    Returns:
        dict: A user shopping cart with the items from notes.

    Example:
    >>> read_notes(('Banana','Apple', 'Orange'))
    {'Banana': 1, 'Apple': 1, 'Orange': 1}
    """
    cart = dict()
    return add_item(cart, notes)

    # Solution by jeffdparker
    """
    return {item: 1 for item in notes}

    This is a dict comprehension. It iterates through in notes and
    makes a dictionary with every item. The quantity added will always
    be 1, as requested.
    """

    # Solution by yawpitch
    """
    return dict.fromkeys(notes, 1)
    """

    # Solution by IsaacG
    """
    return add_item({}, notes)
    """


# 3. Update recipe "ideas" section
"""
The app has an "ideas" section that's filled with finished recipes from
various cuisines. The user can select any one of these recipes and have
all its ingredients added to their shopping cart automatically.

The project manager has asked you to create a way to edit these "ideas"
recipes, since the content team keeps changing around ingredients and
quantities.

Create the function update_recipes(<ideas>, <recipe_updates>) that takes
an "ideas" dictionary and an iterable of recipe updates as arguments.

The function should return the new/updated "ideas" dictionary.
"""


def update_recipes(ideas, recipe_updates):
    """
    Update the recipe ideas dictionary.

    Args:
        ideas (dict): The "recipe ideas" from the ideas section.
        recipe_updates (dict): Updates for the recipes.

    Returns:
        dict: The "recipe ideas" updated.


    >>>update_recipes(
    # ideas
        {'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
         'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}},
    # recipe_updates
        (('Banana Bread', {'Banana': 4,  'Walnuts': 2, 'Flour': 1, 'Butter': 1, 'Milk': 2, 'Eggs': 3}),)
    )
    ...
    {'Banana Bread': {'Banana': 4, 'Walnuts': 2, 'Flour': 1, 'Butter': 1, 'Milk': 2, 'Eggs': 3}, 
    'Raspberry Pie': {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}}
    """
    ideas.update(recipe_updates)
    return ideas

    # Solution by IsaacG
    """
    return ideas | dict(recipe_updates)
    """


# 4. Sort the items in the user cart
"""
Once a user has started a cart, the app allows them to sort their items
alphabetically. This makes things easier to find and helps when there are
data-entry errors like having 'potatoes' and 'Potato' in the database.

Create the function sort_entries(<cart>) that takes a shopping cart/dictionary
as an argument and returns a new, alphabetically sorted one.
"""


def sort_entries(cart):
    """
    Sorts a user's shopping cart in alphabetical order.

    Args:
        cart (dict): A user's shopping cart.

    Returns:
        dict: User's shopping cart sorted alphabetically.
    """
    return dict(sorted(cart.items()))


# 5. Send user shopping cart to store for fulfillment
"""
The app needs to send a given users cart to the store for fulfillment.

However, the shoppers in the store need to know which store aisle the
item can be found in and if the item needs refrigeration.

So (rather arbitrarily) the "fulfillment cart" needs to be sorted in
reverse alphabetical order with item quantities combined with location
and refrigeration information.

Create the function send_to_store(<cart>, <aisle_mapping>) that takes a
user shopping cart and a dictionary that has store aisle number and a
True / False for refrigeration needed for each item.

The function should return a combined "fulfillment cart" that has
(quantity, aisle, refrigeration) for each item the customer is ordering.
Items should appear in reverse alphabetical order.

>>> send_to_store({'Banana': 3, 'Apple': 2, 'Orange': 1, 'Milk': 2},
                  {'Banana': ['Aisle 5', False],
                   'Apple': ['Aisle 4', False],
                   'Orange': ['Aisle 4', False],
                   'Milk': ['Aisle 2', True]}
                )
{'Orange': [1, 'Aisle 4', False],
 'Milk': [2, 'Aisle 2', True],
 'Banana': [3, 'Aisle 5', False],
 'Apple': [2, 'Aisle 4', False]}
"""


def send_to_store(cart, aisle_mapping):
    for key in cart:
        aisle_mapping[key].insert(0, cart[key])
        cart[key] = aisle_mapping[key]
    return dict(reversed(sorted(cart.items())))

    # Solution by jeffdparker
    """
    return {
        key: [value] + aisle_mapping[key]
        for key, value in sorted(cart.items(), reverse = True)
    }

    
    cart.items() = dict_items([(<key_1>, <value_1>), (<key_2>, <value_2>)...])
    """


# 6. Update the store inventory to reflect what a user has ordered
"""
The app can't just place customer orders endlessly. Eventually the store is
going to run out of various products. So your app MVP needs to update the
store inventory every time a user sends their order to the store. Otherwise
customers will order products that aren't actually available.

Create the function update_store_inventory(<fulfillment_cart>, <store_inventory>)
that takes a fulfillment cart and a store inventory.

The function should reduce the store inventory amounts by the number "ordered"
in the "fulfillment cart" and then return the updated store inventory.

Where a store item count falls to 0 the count should be replaced by the message
"Out of Stock".
"""


def update_store_inventory(fulfillment_cart, store_inventory):
    for item, [quantity, aisle, refrigeration] in fulfillment_cart.items():
        store_inventory[item][0] -= quantity
        if store_inventory[item][0] == 0:
            store_inventory[item][0] = "Out of Stock"
    return store_inventory

    # Solution by IsaacG
    """
    return {
        item: [count - fulfillment_cart.get(item, [0])[0] or "Out of Stock", aisle, val]
        for item, (count, aisle, val) in store_inventory.items()
    }
    """
