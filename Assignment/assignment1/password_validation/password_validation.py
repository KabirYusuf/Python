def password_validation(password):
    special_character = ['@', '.', '?', '!', '#', '$', '%', '^', '&', '*', '=', '+', ',', '|']

    validation = True

    if len(password) < 6:
        print("Password character is less than 6")
        validation = False

    if not any(char.isdigit() for char in password):
        print("Password should have at least one digit")
        validation = False

    if not any(char.isupper() for char in password):
        print("Password should have at least one uppercase letter")
        validation = False

    if not any(char.islower() for char in password):
        print("Password should have at least one lowercase letter")
        validation = False

    if not any((char in special_character for char in password)):
        print("Password should contain at least one special character")
        validation = False

    if validation:
        return validation


password: str = str(input("Enter Password: "))
if password_validation(password):
    print("Valid password")

else:
    print("Invalid Password")
