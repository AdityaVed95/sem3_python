"""A module for demonstrating exceptions"""


def convert(s):
    """Convert to an integer"""

    x = -1

    try:
        x = int(s)

    except (ValueError, TypeError):
        pass

    return x

# use ctrl / for commenting and uncommenting multiple lines

# method 2:

#
# def convert(s):
#     """Convert a string to an integer."""
#     try:
#         return int(s)
#
#     except (ValueError, TypeError):
#         return -1
