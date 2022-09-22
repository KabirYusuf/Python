def largest_number(my_list):
    largest = my_list[0]
    for i in my_list:
        if i > largest:
            largest = i
    return largest


def reverse_array(my_list):
    reverse = my_list[::-1]
    return reverse


def is_contain(my_list, number):
    for i in my_list:
        if i == number:
            return True
    return False


def odd_number_position_values(my_list):
    values = []
    for i in range(0, len(my_list)):
        if i % 2 != 0:
            values.append(my_list[i])
    return values


def even_number_position_values(my_list):
    values = []
    for i in range(0, len(my_list)):
        if i % 2 == 0:
            values.append(my_list[i])
    return values


def dict_test(iterble: list | str | tuple):
    dict_value = {}
    for i in iterble:
        if i in dict_value:
            dict_value[i] += 1
        else:
            dict_value[i] = 1
    return dict_value


print(dict_test("hello"))

# my_list = [1, 4, 3, 7, 9, 3]
# print(largest_number(my_list))
# print(reverse_array(my_list))
# print(is_contain(my_list, 44))
# print(odd_number_position_values(my_list))
# print(even_number_position_values(my_list))
