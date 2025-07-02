# Personal notes
"""
This learning exercise helped evolve your knowledge of Comparisons.

Python supports the following basic comparison operators:
   >
   <
   ==
   >=
   <=
   !=
   is       'identity'. 'a is b' is True if and only if a and b are the same object. id(a) == id(b).
   is not
   in       'containment test'. 'a in b' is True if a is a member, subset or element of b
   not in
>>> a = 2
>>> b = a
>>> id(a)
140731312915400
>>> id(b)
140731312915400
>>> a is b
True
>>> a = 3
>>> b = 3
>>> id(a)
140731312915432
>>> id(b)
140731312915432
>>> a is b
True

Strings are compared lexicographically, using individual Unicode code points.
>>> 'Python' > 'Rust'
False
>>> 'Python' > 'Java'
True
>>> '예쁜' < '아름다운'   # example of 'Pretty' < 'Beautiful' in Korean.
False
>>> ord('예'), ord('아')   # can use ord() to check the Unicode code
(50696, 50500)

You can use comparison chaining in any combination and any length.
>>> x = 2
>>> y = 5
>>> z = 10
>>> x < y < z
True

Membership comparisons checks if a value is an element of something.
>>> lucky_numbers = {11, 22, 33}
>>> 22 in lucky_numbers
True
>>> 44 in lucky_numbers
False

Membership comparisons work only with keys for dictionaries.
>>> employee = {'name': 'John Doe', 
                'id': 67826, 'age': 33, 
                'title': 'ceo'}
>>> 'age' in employee
True
>>> 33 in employee
False
>>> 'lastname' not in employee
True

You can also check substrings in strings.
>>> name = 'Super Batman'
>>> 'Bat' in name
True
>>> 'Batwoman' in name
False
"""

# Instructions
"""
In this exercise you are going to implement some rules of Blackjack,
such as the way the game is played and scored.

Note : In this exercise, A means ace, J means jack, Q means queen,
and K means king. Jokers are discarded.
A standard French-suited 52-card deck is assumed, but in most versions,
several decks are shuffled together for play.
"""

# 1. Calculate the value of a card
"""
In Blackjack, it is up to each individual player if an ace is worth
1 or 11 points (more on that later). Face cards (J, Q, K) are scored
at 10 points and any other card is worth its "pip" (numerical) value.

Define the value_of_card(<card>) function with parameter card.
The function should return the numerical value of the passed-in card string.

Since an ace can take on multiple values (1 or 11), this function should fix
the value of an ace card at 1 for the time being. Later on, you will implement
a function to determine the value of an ace card, given an existing hand.
"""


def value_of_card(card):
    """
    Evaluates the numerical value of the passed-in card string.

    * A = 1 point by default
    * J, Q, K = 10 poins
    * Numerical cards are worth its "pip" value. (2 = 2, 3 = 3...)

    Args:
        card (str): Card to be evaluated.

    Returns:
        int: Value of the passed-in card.

    Examples:
        >>> value_of_card('K')
        10
        >>> value_of_card('4')
        4
        >>> value_of_card('A')
        1
    """
    values = {
        'A': 1,
        'K': 10,
        'Q': 10,
        'J': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2
    }
    return values[card.upper()]   # .upper() ensures a capitalized letter

    # Invalid passed-in card handling alternatives
    """
        # Alternative 1
        value = values.get(card.upper())
        if value is None:
            raise ValueError(f"Invalid card: '{card}'")
        return value

        # Alternative 2
        # This alternative is worse because the 'magic string' "Not found" could
        # be used somewhere else in the code, and this would mess up the logic.
        value = values.get(card.upper(), "Not found")
        if value == "Not found":
            raise ValueError(f"Invalid card: '{card}'")
        return value
    """
    # Cool implementation from IsaacG
    """
    if card in "JQK":
        return 10
    if card == "A":
        return 1
    return int(card)
    """


# 2. Determine which card has a higher value
"""
Define the higher_card(<card_one>, <card_two>) function having parameters
card_one and card_two. For scoring purposes, the value of J, Q or K is 10.

The function should return which card has the higher value for scoring.
If both cards have an equal value, return both.
Returning both cards can be done by using a comma in the return statement:
"""


def higher_card(card_one, card_two):
    """
    Determines which of the passed-in cards has a higher value.

    If both cards have an equal value, the function returns both.

    The value for Ace ('A') is predefined in value_of_card().

    Args:
        card_one (str): Card one, passed-in as a "pip" ('A', 'K', '2'...).
        card_two (str): Card two, passed-in as a "pip" ('A', 'K', '2'...).

    Returns:
        str: If one card has a higher value than the other card.
        tuple[str, str]: If both cards have the same value.
    """
    # This way we avoid calling value_of_card() multiple times and
    # make it easier for mainantence
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one
    if value_one < value_two:
        return card_two
    return card_one, card_two


# 3. Calculate the value of an ace
"""
As mentioned before, an ace can be worth either 1 or 11 points.
Players try to get as close as possible to a score of 21 without going
over 21 (going 'burst').

Define the value_of_ace(<card_one>, <card_two>) function with parameters
card_one and card_two, which are a pair of cards already in the hand
before getting an ace card.

Your function will have to decide if the upcoming ace will get a value
of 1 or a value of 11 and return that value.

Remember: the value of the hand with the ace needs to be as high as possible
without going over 21.

Hint: if we already have an ace in hand, then the value for the upcoming ace
would be 1.
"""


def value_of_ace(card_one, card_two):
    """
    Determines the best value (1 or 11) for an upcoming Ace ('A') card.

    Args:
        card_one (str): Card one already in hand, passed-in as a "pip" ('A', 'K', '2'...).
        card_two (str): Card two already in hand, passed-in as a "pip" ('A', 'K', '2'...).

    Returns:
        int: Either '1' or '11', depending on which is better to get as possible
        to 21 without going over 21.

    Examples:
        >>> value_of_ace('6', 'K')
        1
        >>> value_of_ace('7', '3')
        11
    """
    if card_one.upper() == 'A' or card_two.upper() == 'A':   # .upper() ensures a capitalized letter
        return 1

    if value_of_card(card_one) + value_of_card(card_two) + 11 <= 21:
        return 11
    return 1


# 4. Determine a "Natural" or "Blackjack" Hand
"""
If a player is dealt an ace ('A') and a ten-card (10, 'K', 'Q' or 'J') as
their first two cards, then the player has a score of 21. This is known as
a blackjack hand.

Define the is_blackjack(<card_one>, <card_two>) function with parameters
card_one and card_two, which are a pair of cards.
Determine if the two-card hand is a blackjack and return the boolean 'True'
if it is or 'False' otherwise.

Note: the score calculation can be done in many ways. But if possible, we'd
like you to check if there is an ace and a ten-card in the hand (or at a
certain position), as opposed to summing the hand values.
"""


def is_blackjack(card_one, card_two):
    """
    Checks if the starting hand is a Blackjack hand.

    A hand is said to be Blackjack if it has an ace and a 10-value card,
    which would result in 21.

    Args:
        card_one (str): Card one already in hand, passed-in as a "pip" ('A', 'K', '2'...).
        card_two (str): Card two already in hand, passed-in as a "pip" ('A', 'K', '2'...).

    Returns:
        bool: True if the passed-in hand is a Blackjack hand, False otherwise.

    Examples:
        >>> is_blackjack('A', 'K')
        True
        >>> is_blackjack('10', '9')
        False
    """
    tens = {'10', 'J', 'Q', 'K'}   # creates a set of the 10-value "pips"
    cards_in_hand = {card_one.upper(), card_two.upper()}

    # 'cards_in_hand & tens' returns a set with the common elements.
    # >>> cards_in_hand = {'K', '10'}
    # >>> cards_in_hand & tens
    # {'K', '10'}
    # >>> cards_in_hand = {'J', '2'}
    # >>> cards_in_hand & tens
    # {'J'}
    # >>> cards_in_hand = {'4', '9'}
    # >>> cards_in_hand & tens
    # {}

    # bool(x) converts the value x to a boolean (True or False).
    # >>> bool(0)
    # False
    # >>> bool(1)
    # True
    # >>> bool('')
    # False
    # >>> bool('Hi!')
    # True
    # >>> bool([])
    # False
    # >>> bool([1, 2])
    # True
    return 'A' in cards_in_hand and bool(cards_in_hand & tens)


# 5. Splitting pairs
"""
If the player's first two cards are of the same value, such as two sixes,
or a 'Q' and a 'K', a player may choose to treat them as two separate hands.
This is known as "splitting pairs".

Define the can_split_pairs(<card_one>, <card_two>) function with parameters
card_one and card_two, which are a pair of cards.

Determine if this two-card hand can be split into two pairs.
If the hand can be split, return the boolean True. Otherwise, return False.
"""


def can_split_pairs(card_one, card_two):
    """
    Checks if a passed-in pair of cards can be turned into a split hand.

    The function uses another function internally that handles capital mismatches ('a' and 'A').

    Args:
        card_one (str): Card one, passed-in as a "pip" ('A', 'K', '2'...).
        card_two (str): Card two, passed-in as a "pip" ('A', 'K', '2'...).

    Returns:
        bool: True if the hand can be split, False otherwise.

    Examples:
        >>> can_split_pairs('Q', 'K')
        True
        >>> can_split_pairs('10', 'A')
        False
    """
    return value_of_card(card_one) == value_of_card(card_two)


# 6. Doubling down
"""
When the original two cards dealt total 9, 10 or 11 points, a player
can place an additional bet equal to their original bet. This is known
as 'doubling down'.

Define the can_double_down(<card_one>, <card_two>) function with
parameters card_one and card_two, which are a pair of cards.
Determine if the two-card hand can be 'doubled down' and return the
boolean True or False accordingly.
"""


def can_double_down(card_one, card_two):
    if value_of_card(card_one) + value_of_card(card_two) in (9, 10, 11):
        return True
    return False
