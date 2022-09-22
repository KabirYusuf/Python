import string


# word = input("What would you like to encode ")
#
# key = int(input("Your key? "))
#
# lower_letters = string.ascii_lowercase
#
# upper_letters = string.ascii_uppercase
#
# lower_letters_code = lower_letters[key:] + lower_letters[:key]
#
# upper_letters_code = upper_letters[key:] + upper_letters[:key]
#
# letters = lower_letters + upper_letters
#
# letters_code = lower_letters_code + upper_letters_code
#
# encoded_word = word.translate(str.maketrans(letters, letters_code))
#
# print(encoded_word)
#
# decoded_word = encoded_word.translate(str.maketrans(letters_code, letters))
#
# print(decoded_word)

# print("Now, the brute force approach")
#
# for i in range(1, 27):
#     lower_letters_code = lower_letters[i:] + lower_letters[:i]
#
#     upper_letters_code = upper_letters[i:] + upper_letters[:i]
#
#     # encoded_word.translate(str.maketrans(letters, letters_code))
#
#     letters = lower_letters + upper_letters
#
#     letters_code = lower_letters_code + upper_letters_code
#
#     print(encoded_word.translate(str.maketrans(letters_code, letters)))


def encoding(word, key):
    # word = input("What would you like to encode ")

    # key = int(input("Your key? "))

    lower_letters = string.ascii_lowercase

    upper_letters = string.ascii_uppercase

    lower_letters_code = lower_letters[key:] + lower_letters[:key]

    upper_letters_code = upper_letters[key:] + upper_letters[:key]

    letters = lower_letters + upper_letters

    letters_code = lower_letters_code + upper_letters_code

    encoded_word = word.translate(str.maketrans(letters, letters_code))

    print(encoded_word)


encoding("ade is coming", 5)


def decoding(encoded_word, key):
    lower_letters = string.ascii_lowercase

    upper_letters = string.ascii_uppercase

    # decoded_word = encoded_word.translate(str.maketrans(letters_code, letters))

    # print(decoded_word)

    print("Now, the brute force approach")

    # for i in range(1, 27):
    lower_letters_code = lower_letters[key:] + lower_letters[:key]

    upper_letters_code = upper_letters[key:] + upper_letters[:key]

        # encoded_word.translate(str.maketrans(letters, letters_code))

    letters = lower_letters + upper_letters

    letters_code = lower_letters_code + upper_letters_code

    print(encoded_word.translate(str.maketrans(letters_code, letters)))


decoding("fij nx htrnsl", 5)
