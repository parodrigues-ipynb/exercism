# Personal notes
'''
This learning exercise helped evolve your knowledge of Numbers.

There are 3 kinds of built-in numbers in Python.

1. <int>   1234, -10, 20201278
    Integers have arbitrary precision in Python, meaning the number of digits in limited only by the
    available memory of the of the host system.

2. <float>   0.0, 3.14, -9.01
    Floats are usually implemented in Python using a <double> in C (15 decimal places of precision)

3. <complex>   1 + 2j
    Complex are usually used for math wizardry.
    You can extract each part of a complex number z with z.real and z.imag.
    Each part is a float.
    >>> a = 1 + 2j
    >>> a.real
    1.0
    >>> a.imag
    2.0

Python fully supports arithmetic between <int> and <float>.
The <int> is widened to <float>.
>>> 3 + 4.0
7.0
>>> 3 * 4.0
12

Thre are different types of division.

<int> / <int> = <float>
>>> 3 / 3
1.0

<int> // <int> = <int>
>>> 3 // 3
1
>>> 7 // 4
1

<float> // <int> = <float>
<int> // <float> = <float>
>>> 96.40 // 20
4.0

Calculating remainders is similar to other programming languages.
>>> 7 % 4
3
'''

# Instructions
'''
Your friend Chandler plans to visit exotic countries all around the world.
Sadly, Chandler's math skills aren't good.
He's pretty worried about being scammed by currency exchanges during his trip -
and he wants you to make a currency calculator for him.
Here are his specifications for the app:
'''

# 1. Estimate value after exchange
'''C
Create the exchange_money() function, taking 2 parameters:

    budget : The amount of money you are planning to exchange.
    exchange_rate : The amount of domestic currency equal to one unit of foreign currency.

This function should return the value of the exchanged currency.

Note: If your currency is USD and you want to exchange USD for EUR with an exchange rate of 1.20, then 1.20 USD == 1 EUR.
'''
def exchange_money(budget, exchange_rate):
    '''
    Calculates the value of exchanged currency.

    Args:
        budget (float): The amount of money you are planning to exchange.
        exchange_rate (float): The amount of domestic currency equal to one unit of foreign currency.

    Returns:
        float: The value of the exchanged currency.

    Examples:
        >>> exchange_money(127.5, 1.2)
        106.25
    '''
    return budget / exchange_rate

# 2. Calculate currency left after an exchange
'''
Create the get_change() function, taking 2 parameters:

    budget : Amount of money before exchange.
    exchanging_value : Amount of money that is taken from the budget to be exchanged.

This function should return the amount of money that is left from the budget.
'''
def get_change(budget, exchanging_value):
    '''
    Calculates the amount of money that is left from the budget after an exchange.

    Args:
        budget (float): The amount of money before exchange.
        exchanging_value (float): Amount of money that is taken from the budget to be exchanged.

    Returns:
        float: Amount of money that is left from the budget.

    Examples:
        >>> get_change(127.5, 120)
        7.5
    '''
    return budget - exchanging_value

# 3. Calculate value of bills
'''
Create the get_value_of_bills() function, taking 2 parameters:

    denomination : The value of a single bill.
    number_of_bills : The total number of bills.

This exchanging booth only deals in cash of certain increments.
The total you receive must be divisible by the value of one "bill" or unit,
which can leave behind a fraction or remainder.
Your function should return only the total value of the bills
(excluding fractional amounts) the booth would give back.
Unfortunately, the booth gets to keep the remainder/change as an added bonus.
'''
def get_value_of_bills(denomination, number_of_bills):
    '''
    Calculates the total _whole_ value of the bills the exchange booth would give back.

    Args:
        denomination (float): The value of a single bill.
        number_of_bills (int): The total number of bills.

    Returns:
        int: The total value of the bills (excluding fractional amounts) the booth would give back.

    Examples:
        >>> get_value_of_bills(5, 128)
        640
    '''
    return int(denomination * number_of_bills)

# 4. Calculate number of bills
'''
Create the get_number_of_bills() function, taking amount and denomination.

This function should return the number of currency bills that you can receive
within the given amount. In other words: How many whole bills of currency fit
into the starting amount? Remember -- you can only receive whole bills,
not fractions of bills, so remember to divide accordingly.
Effectively, you are rounding down to the nearest whole bill/denomination.
'''
def get_number_of_bills(amount, denomination):
    '''
    Calculates the number of currency bills that you can receive within the given amount.

    Args:
        amount (float): The total number of bills.
        denomination (float): The value of a single bill.

    Returns:
        int: The number of currency bills that you can receive within the given amount.
        Or, "_how many whole bills of currency fit into the starting amount?_"

    Examples:
        >>> get_number_of_bills(127.5, 5)
        25
    '''
    return int(amount // denomination)   # Needs to use int() to ensure the return of an integer.

# 5. Calculate leftover after exchanging into bills
'''
Create the get_leftover_of_bills() function, taking amount and denomination.

This function should return the leftover amount that cannot be returned from
your starting amount given the denomination of bills.
It is very important to know exactly how much the booth gets to keep.
'''
def get_leftover_of_bills(amount, denomination):
    '''
    Calculates the leftover amount from an exchange.

    Args:
        amount (float): The total number of bills.
        denomination (float): The value of a single bill.

    Returns:
        float: Leftover amount that cannot be returned from your starting amount given the denomination of bills.

    Examples:
        >>> get_leftover_of_bills(127.5, 20)
        7.5
    '''
    return amount % denomination

# 6. Calculate value after exchange
'''
Create the exchangeable_value() function, taking budget, exchange_rate, spread, and denomination.

Parameter spread is the percentage taken as an exchange fee, written as an integer.
It needs to be converted to decimal by dividing it by 100.
If 1.00 EUR == 1.20 USD and the spread is 10, the actual exchange rate will be:
1.00 EUR == 1.32 USD because 10% of 1.20 is 0.12, and this additional fee is added to the exchange.

This function should return the maximum value of the new currency after calculating the exchange
rate plus the spread. Remember that the currency denomination is a whole number, and cannot be sub-divided.

Note: Returned value should be int type.
'''
def exchangeable_value(budget, exchange_rate, spread, denomination):
    '''
    Calculates the maximum value of whole bills you can get of a new currency.

    Args:
        budget (float): The amount of money you are planning to exchange.
        exchange_rate (float): The amount of domestic currency equal to one unit of foreign currency.
        spread (float): The percentage taken as an exchange fee, written as an integer.
                If 1.00 EUR == 1.20 USD and the spread is 10, the actual exchange rate will be
                1.00 EUR == 1.32 USD, because 10% of 1.20 is 0.12, and this additional fee is
                added to the exchange.
        denomination (float): The value of a single bill.

    Returns:
        int: The maximum value of the new currency after calculating the exchange rate plus the spread.

    Examples:
        >>> exchangeable_value(127.25, 1.20, 10, 20)
        80
        >>> exchangeable_value(127.25, 1.20, 10, 5)
        95
    '''
    adjusted_exchange_rate = exchange_rate + exchange_rate * spread / 100
    exchanged_budget = exchange_money(budget, adjusted_exchange_rate)
    return int(exchanged_budget - get_leftover_of_bills(exchanged_budget, denomination))