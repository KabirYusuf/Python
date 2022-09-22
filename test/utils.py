# def add(x, y):
#     assert isinstance(x(int, float)) and isinstance(y(int, float)), "only int or float can be added"
#     assert x > 0 and y > 0, "number cannot be negative"
#
#     return x + y
#
#
# print(add("2", "5"))


# def add_list(x: list, y: list) -> list:
#     assert isinstance(x, list) and isinstance(y, list), "Only list can be accepted"
#     return x + y
#
#
# lst2 = [3, 4, 6]
# lst = 1
#
# print(add_list(lst, lst2))

import doctest

from test.exception import MyCustomException


def add(x, y):
    """adds two numbers
    >>> add(5,5)
    11
    >>> add(2, -6)
    -4
    >>> add(2, "hi")
    Traceback (most recent call last)

    """
    if x > y:
        raise MyCustomException("Just fooling around")
    return x + y


print(add(3, 4))
if __name__ == "__main__":
    doctest.testmod()
