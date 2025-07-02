# Personal notes
"""
This learning exercise helped evolve your knowledge of Conditionals.

Python uses if, elif and else to control the flow of execution.

Unlike many other programming languages, Python does not offer a formal case-switch statement.
Instead, Python uses multiple elif statements to serve a similiar purpose.

Python 3.10 introduces a variant case-switch statement called 'structural pattern matching'.
"""

# Instructions
"""
In this exercise, we'll develop a simple control system for a nuclear reactor.

For a reactor to produce the power it must be in a state of criticality.
If the reactor is in a state less than criticality, it can become damaged.
If the reactor state goes beyond criticality, it can overload and result in a meltdown.
We want to mitigate the chances of meltdown and correctly manage reactor state.

The following three tasks are all related to writing code for maintaining ideal reactor state.
"""

# 1. Check for criticality
"""
The first thing a control system has to do is check if the reactor is balanced in criticality.
A reactor is said to be critical if it satisfies the following conditions:

    The temperature is less than 800 K.
    The number of neutrons emitted per second is greater than 500.
    The product of temperature and neutrons emitted per second is less than 500000.

Implement the function is_criticality_balanced() that takes temperature measured in kelvin and
neutrons_emitted as parameters, and returns True if the criticality conditions are met, False if not.
"""


def is_criticality_balanced(temperature, neutrons_emitted):
    """
    Checks if the criticality conditions are met.

    Criticality conditions:
    * Temperature < 800K
    * Number of neutrons emitted per second > 500n/s
    * Product (Temperature * number of neutrons emitted per second) < 500000Kn/s

    Args:
        temperature (float): Core temperature of the reactor, in Kelvin (K)
        neutrons_emitted (int): Number of neutrons emitted per second (n/s)

    Returns:
        bool: True if criticality conditions are met, False if not

    Examples:
        >>> is_criticality_balanced(750, 600)
        True
        >>> is_criticality_balanced(850, 600)
        False
    """
    return (
        temperature < 800 and
        neutrons_emitted > 500 and
        (temperature * neutrons_emitted) < 500000
    )


# 2. Determine the Power output range
"""
Once the reactor has started producing power its efficiency needs to be determined.
Efficiency can be grouped into 4 bands:

* green -> efficiency of 80% or more,
* orange -> efficiency of less than 80% but at least 60%,
* red -> efficiency below 60%, but still 30% or more,
* black -> less than 30% efficient.

The percentage value can be calculated as (generated_power/theoretical_max_power) * 100, where
generated_power = voltage * current. Note that the percentage value of efficiency is usually not an integer number,
so make sure to consider the proper use of the < and <= comparisons.

Implement the function reactor_efficiency(<voltage>, <current>, <theoretical_max_power>),
with three parameters: voltage, current, and theoretical_max_power.
This function should return the efficiency band of the reactor : 'green', 'orange', 'red', or 'black'.
"""


def reactor_efficiency(voltage, current, theoretical_max_power):
    """
    Checks the effiency band of the reactor.

    * Green: 80% <= efficiency
    * Orange: 60% <= efficiency < 80%
    * Red: 30% <= efficiency < 60%
    * Black: efficiency < 30%

    Args:
        voltage (float): Voltage of the reactor, in Volts (V).
        current (float): Current of the reactor, in Ampères (A).
        theoretical_max_power (float): The theoretical power of the reactor, in Watts (W). Must be greater than 0.

    Returns:
        str: the efficiency band of the reactor.

    Examples:
        >>> reactor_efficiency(200, 50, 15000)   # efficiency = 66.6...%
        'orange'
        >>> reactor_efficiency(100, 30, 10000)   # efficiency = 30%
        'red'
        >>> reactor_efficiency(50, 5, 1000)   # efficiency = 25%
        'black'
        >>> reactor_efficiency(400, 50, 25000)   # efficiency = 80%
        'green'
    """
    generated_power = voltage * current
    efficiency = generated_power / theoretical_max_power * 100
    if 80 <= efficiency:
        return 'green'
    if 60 <= efficiency:
        return 'orange'
    if 30 <= efficiency:
        return 'red'
    return 'black'

    # Implementation from IsaacG, uses next()
    """
    levels = (
        (80, "green"),
        (60, "orange"),
        (30, "red"),
        (0, "black")
    )
    # The `levels` tuple NEEDS to be ordered from bigger to smaller in order
      to work with next() in this logic

    efficiency = 100 * (voltage * current) / theoretical_max_power

    return next(color for level, color in levels if efficiency >= level)
    # next() iterates over `levels` in order 80 -> 60 -> 30 -> 0
    # For each (level, color), verifies if efficiency => level
    # next() returns the first color that satisfies efficiency => level
    #
    # next(color for level, color in levels if efficiency >= level) is logically equal to:
    # for level, color in levels:
    #     if efficiency >= level:
    #         return color
    """


# 3. Fail Safe Mechanism
"""
Your final task involves creating a fail-safe mechanism to avoid
overload and meltdown.

This mechanism will determine if the reactor is below, at, or above the
ideal criticality threshold.

Criticality can then be increased, decreased, or stopped by inserting
(or removing) control rods into the reactor.

Implement the function called fail_safe(), which takes 3 parameters:
temperature measured in kelvin, neutrons_produced_per_second, and threshold,
and outputs a status code for the reactor.

* If temperature * neutrons_produced_per_second < 90% of threshold,
  output a status code of 'LOW' indicating that control rods must be
  removed to produce power.

* If the value temperature * neutrons_produced_per_second is within
  10% of the threshold (so either 0-10% less than the threshold, at
  the threshold, or 0-10% greater than the threshold), the reactor is
  in criticality and the status code of 'NORMAL' should be output,
  indicating that the reactor is in optimum condition and control rods
  are in an ideal position.

* If temperature * neutrons_produced_per_second is not in the above-stated
  ranges, the reactor is going into meltdown and a status code of 'DANGER'
  must be passed to immediately shut down the reactor.
"""


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """
    Checks if the reactor is below, at or above the ideal criticality threshold.

    Internally, the reactor_activity (temperature * neutrons_produced_per_second)
    is compared to percentages of the threshold.

    * If reactor_activity < 90% of threshold = 'LOW'
      This band indicates that control rods must be removed to produce power.

    * If 90% <= reactor_activity <= 110% of threshold = 'NORMAL'
      This band indicates that the reactor is in optimum condition and control
      rods are in an ideal position.

    * If 110% of threshold < reactor_activity = 'DANGER'
      This indicates the reactor is going into meltdown and must be immediately
      shut down.

    Args:
        temperature (float): Temperature of the reactor, in Kelvin (K).
        neutrons_produced_per_second (int): Number of neutrons produced per second (n/s).
        threshold (float): Threshold of the status code bands.

    Returns:
        str: Status code ('LOW', 'NORMAL' or 'DANGER')

    Example:
        >>> fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000)
        'DANGER'
    """
    reactor_activity = temperature * neutrons_produced_per_second
    if reactor_activity < (0.9 * threshold):
        return 'LOW'
    if reactor_activity <= (1.1 * threshold):
        return 'NORMAL'
    return 'DANGER'
