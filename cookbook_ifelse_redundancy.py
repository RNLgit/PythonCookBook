"""
Title : cookbook_ifelse_redundancy.py

Description: Ideas of how to redundant if-else or nested if else use to be professional

Author: Runnan Li

**Revision History:**

+---------+------------+------------+-----------------------------------------------------+
| Version |     Date   |   Author   |                  Change Description                 |
+---------+------------+------------+-----------------------------------------------------+
|   0.1   | 23/02/2021 | Runnan Li  |                   Initial Version                   |
+---------+------------+------------+-----------------------------------------------------+
"""


def event_a(arg):
    """
    When you expect to do on event A
    """
    print('Tis is event A. Got argument:', arg)


def event_b(var):
    """
    When you expect to do on event B
    """
    print('This is event B. Gor variable:', var)


if __name__ == "__main__":
    # Map expected signal to function to save if else usage
    map_dict = {
        'trigger event A': event_a,
        'trigger event B': event_b
    }

    # Dummy signal assumption
    signals = {'trigger event A': 1, 'trigger event B': 'B', 'trigger event C': 3}

    for name, var in signals.items():  # iterate dummy signal
        try:
            map_dict[name](var)  # practice to reduce if else usage
        except KeyError:
            print(name, 'not in my know range, cannot execute a corresponding function')  # do on out of scope signals
