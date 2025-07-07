# Personal notes
"""
This learning exercise helped you evolve your knowledge of Lists.

A list is a mutable collection of items in sequence.
* List of numbers                              [1, 2, 3, 4]
* List of strings                              ['1', '2', '3', '4']
* List of both numbers and strings             ['1', 2, '3', 4]
* List of list of numbers and list of strings  [ [1, 2, 3, 4] , ['1', '2', '3', '4']]

You can declare lists in two manners:
* no_elements = list() -> list(1, '2', ['hello'])
* no_elements = []     -> [1, '2', ['hello']]

The list() constructor has a surprising behaviour with strings and dictionaries.
>>> test_for_string = list("test")
>>> test_for_string
['t', 'e', 's', 't']
>>> source_data = {
...     'fish': 'gold',
...     'monkey': 'brown'
...     }
>>> multiple_elements_dict = list(source_data)
['fish', 'monkey']

Lists can be copied in whole or in part via slice notation or <list>.copy().
>>> list_1 = [1, 2, 3, 4]
>>> list_2 = list_1[:-1]
>>> list_2
[1, 2, 3]
>>> list_3 = list_1[0:-1:2]
>>> list_3
[1, 3]

Lists support both common and mutable sequence operations such as:
>>> list = [1, 2, 3, 4]
>>> min(list)
1
>>> max(list)
4
>>> list.index(2)
1
>>> list.append(5)
>>> list
[1, 2, 3, 4, 5]
>>> list.reverse()
>>> list
[5, 4, 3, 2, 1]

To iterate through in a list, you can use the loops
for item in <list>
for index, item in enumerate(<list>)

sum() function returns the sum of all the numbers in the list.
>>> number_list = [1, 2, 3.14, 4, 5/6, 6 + 2j, 7 ** (1/2)]
>>> sum(number_list)
(19.619084644397926 + 2j)

len() function returns the length of the list.
>>> number_list = [1, 2, 3.14, 4, 5/6, 6 + 2j, 7 ** (1/2)]
>>> len(number_list)
7

Lists can be combined in various ways.
>>> new_list_via_concatenate = ['George', 5] + ['cat', 'Tabby']
>>> new_list_via_concatenate
['George', 5, 'cat', 'Tabby']
>>> first_group = ['cat', 'dog', 2]
>>> multiplied_group = first_group * 3
>>> multiplied_group
['cat', 'dog', 2, 'cat', 'dog', 2, 'cat', 'dog', 2]
"""

# Instructions
"""
Elyse is really looking forward to playing some poker (and other
card games) during her upcoming trip to Vegas.

Being a big fan of 'self-tracking', she wants to put together some
small functions that will help her with tracking tasks and has asked
for your help thinking them through.
"""

# 1. Tracking poker rounds
"""
Elyse is specially fond of poker, and wants to track how many rounds
she plays - and which rounds those are.

Every round has its own number, and every table shows the round number
currently being played. Elyse chooses a table and sits down to play
her first round. She plans on playing three rounds.

Implement a function get_rounds(<round_number>) that takes the current
round number and returns a single list with that round and the next two
rounds that are coming up.
"""


def get_rounds(round_number):
    """
    Returns the rounds Elyse will play.

    Args:
        round_number (int): Number of the round currently being played
        at the poker table.

    Returns:
        list: List of the round numbers Elyse will play. This function
        assumes Elyse will always play 3 rounds.

    Examples:
        >>> get_rounds(5):
        [5, 6, 7]
    """
    total_rounds = 3   # total number of rounds Elyse will play
    return [round_number + i for i in range(total_rounds)]
    # Notes on get_rounds()
    """
    range(total_rounds)         -->  0, 1, 2 (immutable)

    round_number + i for i in   -->  round_number + 0
    .                                round_number + 1
    .                                round_number + 2

    [<elements_creation_here>]  -->  creates a list containing the
    .                                elements above
    """


# 2. Keeping all rounds in the same place
"""
Elyse played a few rounds at the first table, then took a break and played
some more rounds at a second table...

...but ended up with a different list for each table!

She wants to put the two lists together so she can track all of the poker
rounds in the same place.

Implement a function concatenate_rounds(<rounds_1>, <rounds_2>) that takes
two lists and returns a list consisting of all the rounds the first list
followed by all the rounds in the second list.
"""


def concatenate_rounds(rounds_1, rounds_2):
    """
    Concatenates two passed-in lists.

    Args:
        rounds_1 (list): The first list.
        rounds_2 (list): The second list to be concatenated with the first list.

    Returns:
        list: A new concatenated list consisting of all elements from the first
        list followed by all the elements from the second list.

    Examples:
        >>> rounds_1 = [1, 2, 3, 4]
        >>> rounds_2 = [6, 7]
        >>> concatenate_rounds(rounds_1, rounds_2)
        [1, 2, 3, 4, 6, 7]
    """
    return rounds_1 + rounds_2


# 3. Finding prior rounds
"""
Talking about some of the prior poker rounds, another player remarks
how similarly two of them played out.

Elyse is not sure if she played those rounds or not.

Implement a function list_contains_round(<rounds>, <round_number>) that
takes two arguments, a list of rounds played by Elyse and a round number.
The function will return 'True' if the round is in the list of rounds
played and 'False' if not.
"""


def list_contains_round(rounds, round_number):
    """
    Checks if <round_number> is an element in the passed-in list <rounds>.

    Args:
        rounds (list): List of the rounds played.
        round_number (int): Number of the round to be found in <rounds>.

    Returns:
        bool: True if <round_number> is in <rounds>, False if not.

    Examples:
        >>> list_contains_round([1, 2, 3], 2)
        True
    """
    return round_number in rounds


# 4. Averaging card values
"""
Elyse wants to try out a new game called Black Joe.

Black Joe is similar to Black Jack, which has a goal of having the
cards in your hand add up to a target value. However, in Black Joe
the goal is to get the average value of the card values to be 7.

Implement a function card_average(<hand>) that will return the average
value of a hand of Black Joe.
"""


def card_average(hand):
    """
    Calculates the average card value of the passed-in hand.

    Args:
        hand (list): List containing the card values in hand.

    Returns:
        float: The average card value in hand.

    Example:
        >>> card_average([5, 6, 7])
        6.0
    """
    return sum(hand) / len(hand) if hand else 0.0
    # Notes on card_average()
    """
    if hand else 0.0  -->  Checks if there is something in the list.
    .                      if there is not, returns 0.0.
    .                      It is done to avoid dividing by 0.
    """


# 5. Alternate averages
"""
Speed is important in Black Joe.

Elyse is going to try and find a faster way of finding the average.

She has thought of two ways of getting an average-like number:
* Take the average of the first and last number in the hand;
* Using the median (middle card) of the hand.

Implement the function approx_average_is_average(<hand>), given hand
a list containg the card values in your hand.

Return True if either one or both of the above written strategies
result in a number equal to the actual average.

Note: the length of all hands is odd to make finding a median easier.
"""


def approx_average_is_average(hand):
    """
    Checks if one or both of the 2 Elyse's strategies are equal to the actual
    average card value in hand.

    The strategies are:
    * Take the average of the first and last number in the hand;
    * Use the median (middle card) of the hand.

    Args:
        hand (list): List of the card values in hand.

    Returns:
        bool: True if at least one of the strategies results in a value equal
        to the average card value in hand, False if not.

    Examples:
        >>> approx_average_is_average([1, 2, 3])
        True
        # middle_card    --> 3 // 2      --> 1 --> hand[1] --> 2
        # approx_average --> (1 + 3) / 2                   --> 2.0
        # card_average   --> 6 / 3                         --> 2.0

        >>> approx_average_is_average([1, 2, 3, 5, 9])
        False
        # middle_card    --> 5 // 2      --> 2 --> hand[2] --> 3
        # approx_average --> (1 + 9) / 2                   --> 5.0
        # card_average   --> 20 / 5                        --> 4.0
    """
    actual_average = card_average(
        hand)   # to avoid calling card_average() 2 times in return comparisons
    middle_card = hand[len(hand) // 2]   # median --> len(hand) // 2
    approx_average = (hand[0] + hand[-1]) / 2

    return approx_average == actual_average or hand[middle_card] == actual_average


# 6. More averaging techniques
"""
Intrigued by the results of her averaging experiment, Elyse is wondering if
taking the average of the cards at the even positions versus the average of
cards at the odd positions would give the same results.

Implement a function average_even_is_average_odd(<hand>) that returns a Boolean
indicating if the average of the cards at even indexes is the same as the average
of the cards at odd indexes.
"""


def average_even_is_average_odd(hand):
    """
    Checks if the average of the cards in the even positions is the same
    as the average of the cards in the odd positions.

    Args:
        hand (list): List of the card values in hand.

    Returns:
        bool: True if the averages are equal, False if not.

    Examples:
    >>> average_even_is_average_odd([1, 2, 3])
    # (1 + 3) / 2 = 2.0
    # 2 / 1       = 2.0
    True

    >>> average_even_is_average_odd([1, 2, 3, 4])
    # (1 + 3) / 2 = 2.0
    # (2 + 4) / 2 = 3.0
    False
    """
    evens = []
    odds = []
    for index, card_value in enumerate(hand):
        if index % 2 == 0:   # checks if the number is even
            evens.append(card_value)
        else:
            odds.append(card_value)

    return card_average(evens) == card_average(odds)

    # Method of list comprehension
    '''
    evens = [card for index, card in enumerate(hand) if index % 2 == 0]
    odds = [card for index, card in enumerate(hand) if index % 2 == 1]
    '''


# 7. Bonus round rules
"""
Every 11th hand in Black Joe is a bonus hand with a bonus rule: if the
last card you draw is a Jack, you double its value.

Implement a function maybe_double_last(hand) that takes a hand and checks
if the last card is a Jack (11). If the last card is a Jack, double its
value before returning the hand.
"""


def maybe_double_last(hand):
    """
    Doubles the value of the last card in the passed-in hand if it's a Jack (11).

    Args:
        hand (list): List of the card values in hand.

    Returns:
        list: The passed-in list with its last card value doubled if it's a Jack (11).

    Examples:
        >>> maybe_double_last([5, 11])
        [5, 22]

        >>> maybe_double_last([5, 6])
        [5, 6]
    """
    if hand and hand[-1] == 11:
        hand[-1] = 11 * 2
    return hand
