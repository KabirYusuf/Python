def add(first_number: int, second_number: int) -> int:
    """

    :param first_number: int
    :param second_number: int
    :return: int
    """

    return first_number + second_number


print(add(8, 7))

print(add.__doc__)


def get_digit(number, position):
    """

    :param number:
    :param position:
    :return:
    """

    return number // (10 ** position) % 10


print(get_digit(1234, 3))


def get_length(number):
    import math
    return math.ceil(math.log10(number))
    """

    :param number:
    :return:
    """


print(get_length(1234))





