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
