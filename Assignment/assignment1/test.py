# h = "Hello World"
#
# h.upper()
# print(h.upper())

# for i in range(1, 21, 2):
#     print(('*' * i).center(20))
#
# print(chr(65))
#
# str_index = "I am testing"
#
# print(str_index[-4])
#
# print(str_index[:7].upper())
#
# print(str_index[::-1])
#
# print(type(str_index))

# river = []
# river_name =['abuja', 'kano', 'bwari']
# for i in range(len(river_name)):
#     print(i, river_name[i])

# user_input: str = input("Enter your name: ")
# user_input = user_input[0:1].upper()
# print(f"The result is {user_input}")
#
# user_input_replace: str = input("enter a text: ").replace("a", "3")
# print(user_input_replace)

# for letters in "python":
#     print(letters)
# letter = "python"
# for i in range(len(letter)):
#     print(letter[i])


def double(number):
    number_double = 2 * number
    return number_double


number = 2
for i in range(1, 4):
    result = double(number)
    number = result
    print(result)
